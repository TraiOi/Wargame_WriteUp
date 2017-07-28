## Challenge 07

| Link |
| ---- |
| view-source:http://hotamago.esy.es/testhacker/sdrawkcab.html |

<p align="center">
  <img src="./Challenge-07-001.png">
</p>

### WriteUp

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
