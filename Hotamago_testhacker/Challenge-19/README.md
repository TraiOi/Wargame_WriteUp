## Challenge 19

| Link |
| ---- |
| http://hotamago.esy.es/testhacker/copassilikeit.php |

<p align="center">
  <img src="./Challenge-19-001.png">
</p>

### WriteUp

- Đù, mã méo gì kia, nhưng mà `viewsource` cái coi có gì hot không, cái page này hay lừa người lắm.
```html
// đường link đây conmeololi.html
// (tin người quá :D)
```

- Tưởng dễ tin hả, không bị lừa đâu :D (Mặc dù có bấm vô link coi thử =))).

- Quay lại đoạn mã hoá thôi, thử hex decode xem.
```
$ echo "6647720b486ec2733da9d7f0b4813ca5" | xxd -r -p
fGr
   HnÂs=©×ð´<¥
```

- Dafug, chắc hàm băm rồi. Phương án này chỉ có thể ngồi bruteforce thôi nhưng có vẻ dễ vi mã chỉ bao gồm số có 4 chữ số.
```
$ str="6647720b486ec2733da9d7f0b4813ca5"; echo ${#str}
32
```

- 32 kí tự thì chắc là MD5 nhỉ. Kệ, quất.

- Đề bài có nói là *mã được mã hoá 2 lần*, kiểu này bruteforce có mà chết, thôi thì đành dùng tool. Vô tình tìm được cái tool decrypt được cái MD5 này :D (http://www.md5online.org/)

- Lần 1:
```
72bcba983cd3b0bf1d4251311d8b3772
```

- Lần 2:
```
5634
```

- Hí hí
```
http://hotamago.esy.es/testhacker/5634.html
```
