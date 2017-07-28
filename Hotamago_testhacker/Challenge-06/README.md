## Challenge 06

| Link |
| ---- |
| http://hotamago.esy.es/testhacker/hotavn.html |

<p align="center">
  <img src="./Challenge-06-001.png">
</p>

### WriteUp

- Bấm thì bấm, ngại gì :v
<p align="center">
  <img src="./Challenge-06-002.png">
</p>

- Lại `promt`, `viewsoure` thôi nào.
```
<center><p>Rất tốt! Level tiếp theo... <a href="sdrawkcab.html">Bấm vào đây</a>.</p></center>
```

- À há, link kìa, quất thôi, đợi gì nữa.
```
http://hotamago.esy.es/testhacker/sdrawkcab.html
```

- 1 `promt` và khi gõ sai password thi sẽ tự redirect về trang level6, nhưng cứ `viewsoure` thôi.
```
view-source:http://hotamago.esy.es/testhacker/sdrawkcab.html
```
```javascript
var pass, i;
pass=prompt("Password: ","");
if (pass=="SAvE-as hELpS a lOt") {
window.location.href="superman.html";
i=4;
}else {alert("Try again");
window.location.href="hotavn.html";}
```

- Chà, có gì khó đâu, pass kìa, nhưng mình cứ bấm link mà triển cho nhanh thôi.
```
http://hotamago.esy.es/testhacker/superman.html
```
