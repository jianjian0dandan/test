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
	diclist = []
	titles = soup.find('table', {'class': 'list-table'}).\
			findAll('a',{'class':'list-title'})
	counts0 = soup.findAll('td',{'class':'last'})
	for count in counts0:
		count = soup.findAll('span')
	num0 = soup.findAll('td',{'class':'first'})
	for num in num0:
		num = soup.findAll('span')
	for x in xrange(len(titles)):
		dic = {}
		dic['No.'] = num[x].string
		dic['counts'] = count[x].string
		dic['title'] = titles[x].string
		dic['url'] = titles[x].get('href')
		diclist.append(dic)

	f = file('/home/gina/python/practice/out.csv','wb')
	writer = csv.writer(f)
	for dic in diclist:
		for dics in dic.iteritems():
			writer.writerow(dics)
	f.close()