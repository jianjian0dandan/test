# -*- coding: utf-8 -*-
import os
import re
import time
import redis
import socket
import pymongo
import datetime


MONGOD_HOST = '219.224.135.47'
MONGOD_PORT = 27019

def default_mongo(host=MONGOD_HOST, port=MONGOD_PORT, usedb='54api_weibo_v2'):
# 强制写journal，并强制safe
    connection = pymongo.MongoClient(host=host, port=port, j=True, w=1)
    db = connection.admin
# db.authenticate('root', 'root')
    db = getattr(connection, usedb)
    return db

def counts():
    db = default_mongo()
    while 1:
        start = db.random_weibo.find().count()
        start_time = time.time()
        print start
        time.sleep(60)
        finish = db.random_weibo.find().count()
        finish_time = time.time()
        counts = finish-start
        print counts ,"in one minute"

if __name__ == '__main__':
    counts()
