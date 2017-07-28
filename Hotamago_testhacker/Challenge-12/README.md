## Challenge 12

| Link |
| ---- |
| http://hotamago.esy.es/testhacker/hw8jfd9.html |

<p align="center">
  <img src="./Challenge-12-001.png">
</p>

### WriteUp

- 1 form đăng nhập bằng PHP.
```html
<h1>Get: unity</h1><br><form method="post" action="phulevel12.php">
<table style="background: gold;" border="2">
<tr><td><strong>User: </strong></td><td><input type="text" name="user"></td></tr>
<tr><td><strong>Pass: </strong></td><td><input type="text" name="pass"></td></tr>
<tr><td><input type="submit" name="login" value="Đăng nhập"></td></tr>
```

- Bấm vô link thử.
```
http://hotamago.esy.es/testhacker/phulevel12.php
```

- Trắng bóc luôn, nhưng ở trang chính có hint cái gì đó "Get: unity". Tham khảo về các method trong HTTP (https://www.w3schools.com/tags/ref_httpmethods.asp)
```
http://hotamago.esy.es/testhacker/phulevel12.php?unity
```

- Hố hố.
```
admin | chucthanhcong!
```
