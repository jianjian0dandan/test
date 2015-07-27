import urllib2

# change followings before use
user = 'foo'
passwd = 'bar'
proxyserver = '1.2.3.4:5'
url   = 'http://www.google.com/'

def proxy3():
    # work for someone, but not for me
    authinfo = urllib2.HTTPBasicAuthHandler()
    authinfo.add_password('realm', proxyserver, user, passwd)
    
    proxy = 'http://%s' % proxyserver
    opener = urllib2.build_opener(urllib2.ProxyHandler( {'http':proxy} ), authinfo)
    urllib2.install_opener(opener)
    
    sContent = urllib2.urlopen(url)
    print sContent.read()