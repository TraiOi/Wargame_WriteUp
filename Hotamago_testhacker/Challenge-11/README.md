## Challenge 11

| Link |
| ---- |
| http://hotamago.esy.es/testhacker/gotodo.php |

<p align="center">
  <img src="./Challenge-11-001.png">
</p>

### WriteUp

- Chả có gì để nhập, chắc là nhập link để "qua bàn".
```html
<body HC="textgame.html">
```

- Bấm vô link thử.
```
http://hotamago.esy.es/testhacker/textgame.html
```
```html
<div style="font-size:3">href code: aHc4amZkOS5odG1s</div>
```

- Cái gì đây? Code? Code gì nhỉ, không có form đăng nhập. Chợt nhớ trang chính có nói gì đó về Base64.
```
$ echo "aHc4amZkOS5odG1s"| base64 -d
hw8jfd9.html
```

- Ý, đúng hướng rồi, tưởng bị lừa chớ :3.
```
http://hotamago.esy.es/testhacker/hw8jfd9.html
```
