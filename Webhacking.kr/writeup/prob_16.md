# Webhacking.kr No.16

## 문제 출제 의도
코드를 이해하고 원하는 바를 접근할 수 있는지 확인한다.

## 소스 코드 분석
```html

<html>
<head>
<title>Challenge 16</title>
<body bgcolor=black onload=kk(1,1) onkeypress=mv(event.keyCode)>
<font color=silver id=c></font>
<font color=yellow size=100 style=position:relative id=star>*</font>
<script> 
document.body.innerHTML+="<font color=yellow id=aa style=position:relative;left:0;top:0>*</font>";

function mv(cd)
{
kk(star.style.posLeft-50,star.style.posTop-50);
if(cd==100) star.style.posLeft=star.style.posLeft+50;
if(cd==97) star.style.posLeft=star.style.posLeft-50;
if(cd==119) star.style.posTop=star.style.posTop-50;
if(cd==115) star.style.posTop=star.style.posTop+50;
if(cd==124) location.href=String.fromCharCode(cd);
}


function kk(x,y)
{
rndc=Math.floor(Math.random()*9000000);
document.body.innerHTML+="<font color=#"+rndc+" id=aa style=position:relative;left:"+x+";top:"+y+" onmouseover=this.innerHTML=''>*</font>";
}

</script>
</body>
</html>
```
* 페이지가 로딩 되면 kk함수를 인자로 1,1을 이용하여 호출한다.

* 키보드를 누를때마다 mv함수를 키보드의 키코드를 인자로 이용하여 호출한다.

* mv 함수는 wasd 키코드에 따라 별이 움직이며 124번 키를 눌렀을 경우 아스키코드 124번에 해당하는 URL로 이동한다.

* kk 함수는 인자의 위치에 별을 찍고 색은 랜덤이다.

## 문제 해결 방안
124 번에 해당하는 키코드를 눌렀을때 이동하는 홈페이지를 들어가면 password가 출력된다.

124 번에 해당하는 아스키 코드는 `|`이다 `|`는 or 연산에 해당하는 문자로 `shift+\`를 눌렀을때 124번 키코드가 입력된다.

이때 출력되는 문자열을 Auth에 입력할 경우 문제풀이에 성공한다.