# Webhacking.kr No.05

## 문제 출제 의도
웹 서버의 폴더구조를 확인해보고 암호화되어 있는 문자열을 복호화하여 코드를 이해할줄 아는지 확인한다.

## 문제 해석
초기에 버튼 두개가 있는 화면에서 로그인을 누르면 로그인 화면으로 페이지가 이동되고, 회원가입을 누르면 Access Denied가 경고창으로 출력된다.

로그인 화면으로 이동하여 URL을 확인하여보면 mem폴더 하단에 login.php가 자리잡고 있음을 볼 수 있다. 따라서 join 또한 mem폴더 하단에 자리잡을것이라는 추측을 할 수 있다.

그를 통하여 join.php에 들어가게 되면 검은화면이 출력되고 코드를 확인하면
```html
<html>
<title>Challenge 5</title></head><body bgcolor=black><center>
<script>
l='a';ll='b';lll='c';llll='d';lllll='e';llllll='f';lllllll='g';llllllll='h';lllllllll='i';llllllllll='j';lllllllllll='k';llllllllllll='l';lllllllllllll='m';llllllllllllll='n';lllllllllllllll='o';llllllllllllllll='p';lllllllllllllllll='q';llllllllllllllllll='r';lllllllllllllllllll='s';llllllllllllllllllll='t';lllllllllllllllllllll='u';llllllllllllllllllllll='v';lllllllllllllllllllllll='w';llllllllllllllllllllllll='x';lllllllllllllllllllllllll='y';llllllllllllllllllllllllll='z';I='1';II='2';III='3';IIII='4';IIIII='5';IIIIII='6';IIIIIII='7';IIIIIIII='8';IIIIIIIII='9';IIIIIIIIII='0';li='.';ii='<';iii='>';lIllIllIllIllIllIllIllIllIllIl=lllllllllllllll+llllllllllll+llll+llllllllllllllllllllllllll+lllllllllllllll+lllllllllllll+ll+lllllllll+lllll;
lIIIIIIIIIIIIIIIIIIl=llll+lllllllllllllll+lll+lllllllllllllllllllll+lllllllllllll+lllll+llllllllllllll+llllllllllllllllllll+li+lll+lllllllllllllll+lllllllllllllll+lllllllllll+lllllllll+lllll;if(eval(lIIIIIIIIIIIIIIIIIIl).indexOf(lIllIllIllIllIllIllIllIllIllIl)==-1) { bye; }if(eval(llll+lllllllllllllll+lll+lllllllllllllllllllll+lllllllllllll+lllll+llllllllllllll+llllllllllllllllllll+li+'U'+'R'+'L').indexOf(lllllllllllll+lllllllllllllll+llll+lllll+'='+I)==-1){alert('access_denied');history.go(-1);}else{document.write('<font size=2 color=white>Join</font><p>');document.write('.<p>.<p>.<p>.<p>.<p>');document.write('<form method=post action='+llllllllll+lllllllllllllll+lllllllll+llllllllllllll+li+llllllllllllllll+llllllll+llllllllllllllll
+'>');document.write('<table border=1><tr><td><font color=gray>id</font></td><td><input type=text name='+lllllllll+llll+' maxlength=5></td></tr>');document.write('<tr><td><font color=gray>pass</font></td><td><input type=text name='+llllllllllllllll+lllllllllllllllllllllll+' maxlength=10></td></tr>');document.write('<tr align=center><td colspan=2><input type=submit></td></tr></form></table>');}
</script>
</body>
</html>
```
이러한 코드가 출력된다.
이 코드의 ll,li와 같은 문자열을 코드에서 제공해준 문자로 치환시켜 주면
```html
<html>
<title>Challenge 5</title></head><body bgcolor=black><center>
<script>
if(eval(docuement.cookie).indexOf(oldzombie)==-1) 
{ bye; }
if(eval(document.URL).indexOf(mode=1)==-1)
{alert('access_denied');history.go(-1);}
else{
    document.write('<font size=2 color=white>Join</font><p>');
    document.write('.<p>.<p>.<p>.<p>.<p>');
    document.write('<form method=post action='+join.php+'>');
    document.write('<table border=1><tr><td><font color=gray>id</font></td><td><input type=text name='+id+' maxlength=5></td></tr>');
    document.write('<tr><td><font color=gray>pass</font></td><td><input type=text name='+pw+' maxlength=10></td></tr>');
    document.write('<tr align=center><td colspan=2><input type=submit></td></tr></form></table>');
}
</script>
</body>
</html>
```
이러한 코드로 나타난다.
이 코드를 이용하여 회원가입을 가능한 창을 출력시키고 그 창에서 회원가입한 admin으로 로그인하면 해결된다.

## 문제 해결 방안
위의 코드를 해석하여 보면 쿠키의 값중에 oldzombie가 있어야 하고, URL에 mode=1이 존재할때 회원가입 폼이 출력된다.

회원가입 폼을 이용하여 admin의 id로 회원가입을 시도하면 이미 존재한 id라는 이유로 실패할 것 이다.

admin값으로 회원가입하기 위하여 다른 방법을 이용하려하면 input태그의 maxlength가 5로 지정되어있어 불가능하기에 maxlength의 값을 바꿔준다.

또한 admin%20이나 admin%00과 같은 문자열을 입력하게되면 php의 insert 버그로 admin 값만이 전달되고 이를 통하여 회원가입에 성공할 수 있다.

이로 회원가입한 admin으로 login해주면 문제풀이에 성공한다.