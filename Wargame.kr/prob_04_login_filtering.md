# Wargame.kr No.04 - login_filtering

## 문제 출제 의도
MySql과 php의 차이를 알고 php를 통한 filtering을 우회할 수 있는지 확인한다.

## 문제 이해
문제에 접근하기 전 힌트에는 `I have accounts. but, it's blocked.    can you login bypass filtering?`가 출력된다.

문제에 접근하게 되면 다음과 같은 코드로 된 페이지가 출력되고 `get source`를 클릭하게 되면 아래와 같은 코드가 출력된다.

```php
<?php

if (isset($_GET['view-source'])) {
    show_source(__FILE__);
    exit();
}

/*
create table user(
 idx int auto_increment primary key,
 id char(32),
 ps char(32)
);
*/

 if(isset($_POST['id']) && isset($_POST['ps'])){
  include("../lib.php"); # include for auth_code function.

  mysql_connect("localhost","login_filtering","login_filtering_pz");
  mysql_select_db ("login_filtering");
  mysql_query("set names utf8");

  $key = auth_code("login filtering");

  $id = mysql_real_escape_string(trim($_POST['id']));
  $ps = mysql_real_escape_string(trim($_POST['ps']));

  $row=mysql_fetch_array(mysql_query("select * from user where id='$id' and ps=md5('$ps')"));

  if(isset($row['id'])){
   if($id=='guest' || $id=='blueh4g'){
    echo "your account is blocked";
   }else{
    echo "login ok"."<br />";
    echo "Password : ".$key;
   }
  }else{
   echo "wrong..";
  }
 }
?>
<!DOCTYPE html>
<style>
 * {margin:0; padding:0;}
 body {background-color:#ddd;}
 #mdiv {width:200px; text-align:center; margin:50px auto;}
 input[type=text],input[type=[password] {width:100px;}
 td {text-align:center;}
</style>
<body>
<form method="post" action="./">
<div id="mdiv">
<table>
<tr><td>ID</td><td><input type="text" name="id" /></td></tr>
<tr><td>PW</td><td><input type="password" name="ps" /></td></tr>
<tr><td colspan="2"><input type="submit" value="login" /></td></tr>
</table>
 <div><a href='?view-source'>get source</a></div>
</form>
</div>
</body>
<!--

you have blocked accounts.

guest / guest
blueh4g / blueh4g1234ps

-->
```
- 위와 같은 코드로 이루어져 있다.
-----
```php
if (isset($_GET['view-source'])) {
    show_source(__FILE__);
    exit();
}
```
- GET 방식으로 view-source를 입력하면 소스를 보여주는 부분이다.
-----
```php

 if(isset($_POST['id']) && isset($_POST['ps'])){
  include("../lib.php"); # include for auth_code function.

  mysql_connect("localhost","login_filtering","login_filtering_pz");
  mysql_select_db ("login_filtering");
  mysql_query("set names utf8");

  $key = auth_code("login filtering");

  $id = mysql_real_escape_string(trim($_POST['id']));
  $ps = mysql_real_escape_string(trim($_POST['ps']));

  $row=mysql_fetch_array(mysql_query("select * from user where id='$id' and ps=md5('$ps')"));

  if(isset($row['id'])){
   if($id=='guest' || $id=='blueh4g'){
    echo "your account is blocked";
   }else{
    echo "login ok"."<br />";
    echo "Password : ".$key;
   }
  }else{
   echo "wrong..";
  }
 }
```
- POST 방식으로 전달받은 id와 pw가 존재한지 확인 하여 소스를 실행하고 존재하지 않다면 실행하지 않는다.

- 쿼리와 연결한다.

- POST 방식으로 전달받은 id와 pw를 통하여 escape 처리하여 쿼리에 대입하여 DB에서 찾는다.

- 결과가 있고 해당하는 id값이 `guest` 혹은 `blueh4g`라면 필터링 해내고 아니라면 로그인에 성공하며 password를 출력해준다.

-----
```php
<!--

you have blocked accounts.

guest / guest
blueh4g / blueh4g1234ps

-->
```
- 위의 코드로 id와 pw를 알려주고 있다.

## 문제 해결 방안
PHP와 MySql의 차이점을 이용한다.

php는 대소문자를 구별하지만 MySql은 구별하지 않는다.

하지만 php에서 query문을 완성하여 mysql에 요청을 할때 pw의 경우 md5방식으로 암호화 하고 있지만 id는 암호화 하지 않고 있기 때문의 php와 MySql의 대소문자 구별 유무를 이용하여 문제를 푸는 것에 접근할 수 있다.

따라서 id를 입력할 때 `guest` 혹은 `blueh4g`를 입력하지 않고 한 문자 이상 대문자로 바꾸어 입력한 후에 비밀번호를 입력하면 flag가 출력되고 해당 flag를 auth에 입력하면 문제 풀이에 성공한다.