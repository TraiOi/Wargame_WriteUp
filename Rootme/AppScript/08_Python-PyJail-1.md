## Python - PyJail 1

| Author | Level | Points |
| ------ | ----- | ------ |
| sambecks | Medium | 35 |


> level 1
>
> **Statement**
>
> Retrieve validation’s password and get out of this jail.

#### Solution

We know the `jail` filtered `__`, `'`, `"`, `import` and `dir`. Every function in Python has a `func_code` property. In `func_code` has a attribute is `co_consts` contains the constants of Python function (try to guess if string must be compared with default variable)

```
>>> print exit.func_code.co_consts
```

```
(None, 'flag-WQ0dSFrab3LGADS1ypA1', -1, 'cat .passwd', 'You cannot escape !')
```

Now, we can get the flag

```
>>> exit(exit.func_code.co_consts[1])
```