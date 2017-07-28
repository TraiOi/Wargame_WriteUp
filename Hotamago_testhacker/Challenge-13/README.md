## Challenge 13

| Link |
| ---- |
| http://hotamago.esy.es/testhacker/hw8jfd91.html |

<p align="center">
  <img src="./Challenge-13-001.png">
</p>

### WriteUp

- 1 source HTML dài thòng lòng, kiểu để nhiều space và break line để lừa ai không chú ý đây mà, nhưng làm sao qua mắt được thánh soi.
```
<!-------------------  Password: ZW15ZXVvbmlpY2hhbg== Thêm phần mở rộng trang vào đó  ----------- >
```

- Định dạng này chỉ có thể là Base64.
```
$ echo "ZW15ZXVvbmlpY2hhbg==" | base64 -d
emyeuoniichan
```

- *Thêm phần mở rộng trang vào đó*, thử nào
```
http://hotamago.esy.es/testhacker/emyeuoniichan.html
```

- Trật lất.
```
http://hotamago.esy.es/testhacker/emyeuoniichan.php
```

- Bingo, next thôi.
