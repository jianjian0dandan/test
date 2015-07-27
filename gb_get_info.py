#-*-coding=utf-8-*-

import urllib2
import sys
import csv
from BeautifulSoup import BeautifulSoup
import gb_find_ip
import os
reload(sys)
sys.setdefaultencoding('utf-8')


host = '202.43.147.226'
port = '8080'
url  = 'http://guba.eastmoney.com/list,601766.html'

def proxy1():
    inside = []
    ipfile = csv.reader(file('/home/gina/python/practice/ip.csv', 'rb'))
    i = 1
    #ipfile = open('ip.csv').readlines()
    for line in ipfile:
        #host = line[0]
        #port = line[1]
        #proxy = 'http://%s:%s' % (host, port)
        proxy = 'http://%s' % (line[0])
        try:
            opener = urllib2.build_opener( urllib2.ProxyHandler({'http':proxy}) )
            urllib2.install_opener(opener)
            sContent = urllib2.urlopen(url)
            content = sContent.read().decode('utf-8','replace')
            a = get_page(content)
            print a,i
            #write('/home/gina/python/practice/ip_use.csv',[host+':'+port])
            write('/home/gina/python/practice/ip_use.csv',line)
            #write('/home/gina/python/practice/gb_out.csv',[a])
            write('/home/gina/python/practice/gb_out.csv',a)
            i = i + 1
        except Exception, e:
            print e
            print line
            i = i + 1
    return inside

def get_page(con):
    titles = []
    soup = BeautifulSoup(con)
    title = soup.find('span',{'id':'stockname'}).find('a').string
    return title

def write(path,names):
    if os.path.exists(path):
        csvfile = open(path, 'ab')
    else:
        csvfile = open(path, 'wb')        
    writer = csv.writer(csvfile)
    for i in names:
        writer.writerow([i])
    csvfile.close()

if __name__ == '__main__':
    #gb_find_ip.ip_spider('/home/gina/python/practice/ip.csv','http://www.xici.net.co/')
    side = proxy1()
    #write(side)
