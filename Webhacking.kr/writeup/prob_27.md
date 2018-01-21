# Webhacking.kr No.27

## 문제 출제 의도
DB 구조를 이해하고 SQL Injection할 수 있는지 확인한다.

## 문제 이해
문제에 접근하면 input 태그와 버튼이 하나 출력된다.

소스코드 보기할 시에 index.phps가 있다는 것을 알 수 있어 접근하여 소스코드를 확인하여 보면 아래와 같은 코드가 출력된다.
```php
<?
if($_GET[no])
{

if(eregi("#|union|from|challenge|select|\(|\t|/|limit|=|0x",$_GET[no])) exit("no hack");

$q=@mysql_fetch_array(mysql_query("select id from challenge27_table where id='guest' and no=($_GET[no])")) or die("query error");

if($q[id]=="guest") echo("guest");
if($q[id]=="admin") @solve();

}

?>
```
* GET 방식으로 전달된 no 값이 있을때 코드가 작동한다.

* GET 방식으로 전달된 no 값을 `#`,`union`,`from`,`challenge`,`select`,`(`,`\t`,`/`,`limit`,`=`,`0x`를 필터링 해낸다.

* GET 방식으로 전달된 no 값으로 SQL 문을 조작하여 SQL문이 올바르지 않다면 `query error`을 출력하고 받아온 값이 `guest`면 `guest`를 출력하며 `admin`이면 문제 풀이에 성공한다.

## 문제 해결 방안
우선 guest의 no값을 알아내기 위하여 숫자를 순서대로 입력해보았는데 1에서 guest가 출력되는것을 보아 DataBase에서 no 가 1번일때 guest임을 알 수 있었다. 

따라서 admin은 2일 것이라 추측할 수 있었다.

위를 통하여 no값을 2로 조작하고 `id='guest'`를 무력시키기 위하여 no가 1이 아닌 다른 값을 입력한후에 or연산으로 no에 2를 입력해주면된다.

하지만 query문에 이미 완성되어 있는 `($_GET[no])`에서 `(`를 무력화 시켜야 쿼리가 올바르게 작동하므로 우선 `no=-1)`과 같이 닫아준다.

그리고 `or no=2`를 입력해야하는데 `=`가 필터링 되고 있으므로 대체 수단인 `like`를 이용한다.

위를 이용하여 no값을 GET방식으로 `no=-1) or no like 2`와 같이 입력하면 `query error`가 출력된다. 이유는 `($_GET[no])`에서 `)`때문인데 `(`는 필터링 있기 때문에 `)`를 무력화 시켜야 한다.

때문에 주석을 이용하여 뒤를 무력화 시키면된다. 

따라서 완성된 URL은 `…?no=-1) or no like 2 -- -`를 하면 문제 풀이에 성공한다.
