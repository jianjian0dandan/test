#!/bin/bash
while ((a = 1));do
   start=$(date "+%s")
   #scrapy crawl search_random_spider --loglevel=INFO --logfile=spider_result.log
   sleep 60s
   now=$(date "+%s")
   time=$((now-start))
   echo "time used:$time seconds"
done  
