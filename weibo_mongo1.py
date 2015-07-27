# -*- coding: utf-8 -*-
import os
import re
import time
import redis
import socket
import pymongo
import datetime
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

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
    '''writer.writerow(["_id","reposts_count","truncated","text","in_reply_to_status_id","id",\
                    "thumbnail_pic","mid","comments","source","attitudes_count",\
                    "in_reply_to_screen_name","in_reply_to_user_id",\
                    "created_at", "id","mid","text","source","favorited","truncated","in_reply_to_status_id",    "in_reply_to_user_id",  "in_reply_to_screen_name","pic_urls","thumbnail_pic","geo","reposts_count","comments_count","attitudes_count"])
    '''
    titles = ["_id","domain","last_modify","id","city","verified","followers_count",\
                    "followers","location","verified_type", "province","statuses_count",\
                    "description","friends_count","first_in","allow_all_act_msg","profile_image_url",\
                    "geo_enabled","friends","favourites_count","name", "url","gender",\
                    "bi_followers_count","verified_reason","timestamp"]
    writer.writerow(title)   

    for uid in uidlist:
        query = {"_id":int(uid)}
        results = db.master_timeline_weibo.find(query)
        for result in results:
            items = []
            items.append(result)
            for item in items:
                for title in titles[:-1]:
                    try: 
                        csvfile.write(str(item[title]) + ",")
                    except KeyError:
                        csvfile.write("null,")
                try: 
                    csvfile.write(str(item["timestamp"]) + ",")
                except KeyError:
                    csvfile.write("\n")
    csvfile.close() 

if __name__ == '__main__':
    out()


