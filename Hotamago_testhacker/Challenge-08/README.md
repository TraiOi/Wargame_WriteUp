## Challenge 08

| Link |
| ---- |
| http://hotamago.esy.es/testhacker/sdrawkcab.html |

<p align="center">
  <img src="./Challenge-08-001.png">
</p>

### WriteUp

- 1 `promt` và cứ `viewsoure` thôi.
```
view-source:http://hotamago.esy.es/testhacker/superman.html
```
```html
<h1>Level 8</h1><SCRIPT SRC="psswd.js" LANGUAGE="JavaScript" type="text/javascript"></script>
```

- Gọi 1 file `js` khác à, nhưng trốn đâu được
```
http://hotamago.esy.es/testhacker/psswd.js
```
```javascript
var pass;
pass=prompt("Password:","");
if (pass=="hackertestz") {
window.location="sieunhanmacsip.html";
}else {
alert("Thá»­ láº¡i...");
}
```

- Chà, có gì khó đâu, pass kìa, nhưng mình lại cứ bấm link mà triển cho nhanh thôi.
```
http://hotamago.esy.es/testhacker/sieunhanmacsip.html
```
