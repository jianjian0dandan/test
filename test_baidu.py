#-*-coding=utf-8-*-

import csv
import urllib2
from BeautifulSoup import BeautifulSoup


def baidu_spider(url):
	data = urllib2.urlopen(url).read()
	soup = BeautifulSoup(data)

	titlelist = []
	urllist = []
	countlist = []
	numberlist = []

	titles = soup.find('table', {'class': 'list-table'}).findAll('a', {'class': 'list-title'})
	for a in titles:
		title = a.string
		titlelist.append(title)
		urls = a.get('href')
		urllist.append(urls)

	count = soup.findAll('span', {'class': 'icon-fall'}) + soup.findAll('span', {'class': 'icon-rise'})
 	for b in count:
 		counts = b.string
 		countlist.append(counts)

	num = soup.findAll('span', {'class': 'num-top'}) + soup.findAll('span', {'class': 'num-normal'})
	for c in num:
		number = c.string
		numberlist.append(number)

	res = zip(numberlist, titlelist, countlist, urllist)

	writer = csv.writer(file('/home/gina/python/practice/out.csv', 'wb'))
	for i in res:
		writer.writerow(i)


if __name__ == '__main__':
	url = 'http://top.baidu.com/buzz?b=1'
	baidu_spider(url)