# Webhacking.kr No.18

## 문제 출제 의도
간단한 SQL Injection을 할 수 있는지 확인한다.

## 소스 코드 분석
```html
<form method=get action=index.php> 
<table border=0 align=center cellpadding=10 cellspacing=0> 
<tr><td><input type=text name=no></td><td><input type=submit></td></tr> 
</table> 
</form> 
```
* form 태그의 GET 방식으로 index.php에 요청한다.

* input 태그의 name이 no인 값을 전달한다.

-----

```php
if($_GET[no]) 
{ 

if(eregi(" |/|\(|\)|\t|\||&|union|select|from|0x",$_GET[no])) exit("no hack"); 

$q=@mysql_fetch_array(mysql_query("select id from challenge18_table where id='guest' and no=$_GET[no]")); 

if($q[0]=="guest") echo ("hi guest"); 
if($q[0]=="admin") 
{ 
@solve(); 
echo ("hi admin!"); 
} 

} 
```
* GET 방식으로 전달된 no의 값이 비어있지 않을때 실행되는 코드이다.

* eregi 함수로 GET 방식으로 전달된 no의 값을 ` `,`/`,`(`,`)`,`\t`,`|`,`&`,`union`,`select`,`from`,`0x`로 필터링 해낸다.

* mysql에서 GET방식의 no 값을 통하여 얻어온 id의 값을 받아와 변수 q에 저장한다.

* 변수 q에 저장된 첫번째 인자값이 guest이면 `hi guest`를 출력하고 admin이면 문제 풀이에 성공한다.

## 문제 해결 방안
우선 Injection으로 no=1을 입력해본 결과 `hello guest`가 출력된 것을 보아 guest의 no값은 1 임을 알 수 있었다.

이때 거의 대부분의 경우가 admin은 no가 2임을 추측할 수 있었다.

이를 이용하여 SQL Injection을 시도해 볼 수 있덨다.

urlencoding을 이용하여 `?no=(1이 아닌 어떤 값)&0Aor%0Ano=2`를 시도해보게 되면 문제 풀이에 성공한다.

이것이 가능한 이유는 우선 띄어쓰기를 필터링하기 때문에 대체 수단인 LineFeed를 이용한 것이고 AND연산이 OR연산보다 우선순위가 높기 때문에 SQL Query상으로

`select id from challenge18_table where (id='guest' and no=3) or no=2` 이런식으로 연산 순서가 이루어 지기 때문이다.