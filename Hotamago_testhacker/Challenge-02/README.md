## Challenge 02

| Link |
| ---- |
| http://hotamago.esy.es/testhacker/34urhef.html |

<p align="center">
  <img src="./Challenge-02-001.png">
</p>

### WriteUp

- Chả có gì đặc biệt, lại `viewsource` for ez life ..
```javascript
//ádasdddddddd//ádasdddddddd//ádasdddddddd
var s1="<h1 style=\"color: red;\">Xin chúc mừng! bạn có năng khiếu hacker đấy!</h1>";
var s2="<h1 style=\"color: red;\">Tài khoản hoặc mật khẩu không đúng!</h1>";
//ádasdddddddd
var qwhj="h7728jds1f";//ádasdddddddd//ádasdddddddd//ádasdddddddd
       function saqưed1145312(){ //ádasdddddddd //ádasdddddddd //ádasdddd//ádasdddddddddddd
   //pass:123345//ádasdddddddd//ádasdddddddd
       var user = document.getElementById("cca").value;//ádasdddddddd//ádasdddddddd
     //pass:2312312//ádasdddddddd//ádasdddddddd//pass:123123124//ádasdddddddd//ádasdddddddd
    var pass = document.getElementById("ada").value;//ádasdddddddd//ádasdddddddd
     //ádasdddddddd //ádasdddddddd //ádasdddddddd//ádasdddddddd//ádasdddddddd
  //ádasdddddddd
  //ádasdddddddd //ádasdddddddd
             if(pass=="admin" && user==qwhj){ //ádasdddddddd //ádasdddddddd
      //ádasdddddddd
     document.getElementById("html").innerHTML = s1; //ádasdddddddd //ádasdddddddd
     window.location="level3.php";
     } //ádasdddddddd//ádasdddddddd//ádasdddddddd//ádasdddddddd
      //ádasdddddddd //ádasdddddddd //ádasdddddddd //ádasdddddddd
     else{
      //ádasdddddddd //ádasdddddddd //ádasdddddddd //ádasdddddddd
     document.getElementById("html").innerHTML = s2; //ádasdddddddd //ádasdddddddd //ádasdddddddd
     } //ádasdddddddd //ádasdddddddd //ádasdddddddd
      //ádasdddddddd //ádasdddddddd
         } //ádasdddddddd //ádasdddddddd
```

- Ú ù, chơi khó nhau đây, nhưng thật chỉ là 1 kiểu obfuscate siêu cơ bản bằng mấy dấu comment thôi mà. Sau khi deobfuscate
```javascript
var qwhj="h7728jds1f";
function saqưed1145312() {
  var user = document.getElementById("cca").value;
  var pass = document.getElementById("ada").value;
  if(pass=="admin" && user==qwhj) {
     document.getElementById("html").innerHTML = s1;
     window.location="level3.php";
  els e{
     document.getElementById("html").innerHTML = s2;
  }
}
```

- Thông tin để "qua bàn"
```
admin | h7728jds1f
```
