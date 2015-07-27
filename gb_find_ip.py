#-*-coding=utf-8-*-

import csv
import urllib2
from BeautifulSoup import BeautifulSoup
import time
import sys
import os


def ip_spider(path,url):
	data = urllib2.urlopen(url).read()
	soup = BeautifulSoup(data)
	ipread = []
	iplist = []

	trs = soup.findAll('tr',{'class':'odd'}) + soup.findAll('tr',{'class':''}) 
	for tr in trs :
		tds = tr.findAll('td')
		ip = tds[2].string
		port = tds[3].string
		address = ip+':'+port
		iplist.append(address)

	if os.path.exists(path):
		ip_file = csv.reader(file(path, 'rb'))
		for line in ip_file :
			ipread.append(line[0])
		csvfile = open(path, 'ab')
		writer = csv.writer(csvfile)
		for i in iplist :
			if i not in ipread:
				writer.writerow([i])
		csvfile.close()
	else:
		csvfile = open(path,'wb')
		writer = csv.writer(csvfile)
		for i in iplist :
			writer.writerow([i])
		csvfile.close()

if __name__ == '__main__':
	for i in range(1,100): #424
		url = 'http://www.xici.net.co/qq/'+ str(i)
		path = '/home/gina/python/practice/ip.csv'
	 	ip_spider(path,url)