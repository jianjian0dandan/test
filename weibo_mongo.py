# -*- coding: utf-8 -*-
import os
import re
import time
import redis
import socket
import pymongo
import datetime
import csv

MONGOD_HOST = '219.224.135.47'
MONGOD_PORT = 27019

def default_mongo(host=MONGOD_HOST, port=MONGOD_PORT, usedb='54api_weibo_v2'):
    connection = pymongo.MongoClient(host=host, port=port, j=True, w=1)
    db = connection.admin
    db = getattr(connection, usedb)
    return db

def read():
    idlist = []
    path = '/home/gina/python/practice/source/all_uidlist.txt'
    uid_file = open(path,'r')
    for line in uid_file:
        idlist.append(line)
    return idlist

def out():
    uidlist = read()
    items = []
    db = default_mongo()
    path = '/home/gina/python/practice/weibo_user.csv'
    csvfile = open(path,'wb')   
    writer = csv.writer(csvfile) 
    writer.writerow(["_id","reposts_count","truncated","text","in_reply_to_status_id","id",\
                    "thumbnail_pic","mid","comments","source","attitudes_count",\
                    "in_reply_to_screen_name","in_reply_to_user_id",\
                    "created_at", "id","mid","text","source","favorited","truncated","in_reply_to_status_id",    "in_reply_to_user_id",  "in_reply_to_screen_name","pic_urls","thumbnail_pic","geo","reposts_count","comments_count","attitudes_count"])
    writer.writerow(["_id","domain","last_modify","id","city","verified","followers_count",\
                    "followers","location","verified_type", "province","statuses_count",\
                    "description","friends_count","first_in","allow_all_act_msg","profile_image_url",\
                    "geo_enabled","friends","favourites_count","name", "url","gender","created_at",\
                    "bi_followers_count","verified_reason","timestamp"])   
    for uid in uidlist:
        query = {"_id":uid}
        results = db.master_timeline_weibo.find(query)
        for result in results:
            items.append(result)

    for item in items:
        #ids = item["id"]
    ''' csvfile.write(str(item["_id"]) + ",")
        csvfile.write(str(item["reposts_count"]) + ",")
        csvfile.write(str(item["truncated"]) + ",")
        csvfile.write(str(item["text"]) + ",")
        csvfile.write(str(item["in_reply_to_status_id"]) + ",")
        csvfile.write(str(item["id"]) + ",")
        csvfile.write(str(item["thumbnail_pic"]) + ",")
        csvfile.write(str(item["mid"]) + ",")
        csvfile.write(str(item["comments"]) + ",")
        csvfile.write(str(item["source"]) + ",")
        csvfile.write(str(item["attitudes_count"]) + ",")
        csvfile.write(str(item["in_reply_to_screen_name"]) + ",")
        csvfile.write(str(item["in_reply_to_user_id"]) + "\n")
    '''
        csvfile.write(str(item["_id"]) + ",")
        csvfile.write(str(item["domain"]) + ",")
        csvfile.write(str(item["last_modify"]) + ",")
        csvfile.write(str(item["id"]) + ",")
        csvfile.write(str(item["city"]) + ",")
        csvfile.write(str(item["verified"]) + ",")
        csvfile.write(str(item["followers_count"]) + ",")
        csvfile.write(str(item["followers"]) + ",")
        csvfile.write(str(item["location"]) + ",")
        csvfile.write(str(item["verified_type"]) + ",")
        csvfile.write(str(item["province"]) + ",")
        csvfile.write(str(item["statuses_count"]) + ",")
        csvfile.write(str(item["description"]) + ",")
        csvfile.write(str(item["friends_count"]) + ",")
        csvfile.write(str(item["first_in"]) + ",")
        csvfile.write(str(item["allow_all_act_msg"]) + ",")
        csvfile.write(str(item["profile_image_url"]) + ",")
        csvfile.write(str(item["geo_enabled"]) + ",")
        csvfile.write(str(item["friends"]) + ",")
        csvfile.write(str(item["favourites_count"]) + ",")
        csvfile.write(str(item["name"]) + ",")
        csvfile.write(str(item["url"]) + ",")
        csvfile.write(str(item["gender"]) + ",")
        csvfile.write(str(item["created_at"]) + ",")
        csvfile.write(str(item["bi_followers_count"]) + ",")
        csvfile.write(str(item["verified_reason"]) + ",")
        csvfile.write(str(item["timestamp"]) + "\n")
    csvfile.close() 

if __name__ == '__main__':
    out()
