# -*- coding: utf-8 -*-

import urllib2
import urllib3
import csv
from BeautifulSoup import BeautifulSoup

class baidu(object):
	def __init__(self):
		user_agent = '''Mozilla/5.0 (X11; Ubuntu; 
						Linux i686; rv:31.0) 
						Gecko/20100101 Firefox/31.0'''
		self.headers = {'User_agent': user_agent}
		self.http_pool = urllib3.connection_from_url(
			"http://top.baidu.com",timeout = 15,
			maxsize = 5, headers = self.headers)

	def urlopen(self,url):
		res = self.http_pool.urlopen('GET',url,headers = 
			self.headers)
		return res.data

if __name__ == '__main__':
	url = 'http://top.baidu.com/buzz?b=1'
	baidu_data = baidu()
	data = urllib2.urlopen(url).read()
	soup = BeautifulSoup(data)
	titlelist = []
	urllist = []
	countlist = []
	numberlist = []
	titles = soup.find('table', {'class': 'list-table'}).\
			findAll('a',{'class':'list-title'})
	for a in titles:
		title = a.string
		titlelist.append(title)
		urls = a.get('href')
		urllist.append(urls)
	count = soup.findAll('span',{'class':'icon-fall'})\
 			+ soup.findAll('span',{'class':'icon-rise'})
 	for b in count:
 		counts = b.string
 		countlist.append(counts)
	num = soup.findAll('span',{'class':'num-top'})\
			+soup.findAll('span',{'class':'num-normal'})
	for c in num:
		number = c.string
		numberlist.append(number)
	res = zip(numberlist,titlelist,countlist,urllist)
	f = file('/home/gina/python/practice/out.csv','wb')
	writer = csv.writer(f)
	for i in res:
		writer.writerow(i)
	f.close()