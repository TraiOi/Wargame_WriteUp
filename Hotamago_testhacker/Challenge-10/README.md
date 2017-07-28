## Challenge 10

| Link |
| ---- |
| http://hotamago.esy.es/testhacker/hanghotaVN.html |

<p align="center">
  <img src="./Challenge-10-001.png">
</p>

### WriteUp

- Lại 1 form đăng nhập.
```html
<form method="post" action="gotodo.php">
<table style="background: gold;" border="2">
<tr><td><strong>User: </strong></td><td><input type="text" name="user"></td></tr>
<tr><td><strong>Pass: </strong></td><td><input type="text" name="pass"></td></tr>
<tr><td><input type="submit" name="login" value="Đăng nhập"></td></tr>
```

- Bấm vô link thử.
```
http://hotamago.esy.es/testhacker/gotodo.php
```

- Ơ đệt, sao dễ hơn trap trước thế ...
