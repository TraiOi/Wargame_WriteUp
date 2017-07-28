## Challenge 20

| Link |
| ---- |
| http://hotamago.esy.es/testhacker/5634.html |

<p align="center">
  <img src="./Challenge-20-001.png">
</p>

### WriteUp

- Khó vãi luôn, tool cũ nhé (http://www.md5online.org/), bấm phát ra luôn.
```
Gh3i
```

- Nếu muốn dùng tool offline đề phòng trường hợp nhà rớt mạng hay cái trang MD5 decrypt kia sập thì cứ dùng `John The Ripper`.
```
$ john --format=raw-md5 hash.txt --incremental:All5
Loaded 1 password hash (Raw MD5 [128/128 AVX intrinsics 12x])
Gh3i             (?)
guesses: 1  time: 0:00:00:13 DONE (Fri Jul 28 11:24:17 2017)  c/s: 3477K  trying: Gh3e - Gh3g
Use the "--show" option to display all of the cracked passwords reliably
```

- Qua luôn
```
http://hotamago.esy.es/testhacker/Gh3i.html
```
