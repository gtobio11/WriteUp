# Wargame.kr No.09 - md5 password

## 문제 출제 의도
md5 함수 두번째 인자 true에 관해서 알고 있는지 확인하고 그를 이용하여 sql injection 할 수 있는지 확인한다.

## 문제 이해 
문제에 접근하기 전에 힌트로써 `md5('value', true);`가 출력된다.

문제에 접근하게 되면 password를 입력할 수 있는 창과 login 버튼이 출력되고 get_source로 소스 코드를 볼 수 있게끔 한다.

아래는 해당 문제의 소스코드이다.
```php
<?php
 if (isset($_GET['view-source'])) {
  show_source(__FILE__);
  exit();
 }

 if(isset($_POST['ps'])){
  sleep(1);
  mysql_connect("localhost","md5_password","md5_password_pz");
  mysql_select_db("md5_password");
  mysql_query("set names utf8");
  /*
  
  create table admin_password(
   password char(64) unique
  );
  
  */

  include "../lib.php"; // include for auth_code function.
  $key=auth_code("md5 password");
  $ps = mysql_real_escape_string($_POST['ps']);
  $row=@mysql_fetch_array(mysql_query("select * from admin_password where password='".md5($ps,true)."'"));
  if(isset($row[0])){
   echo "hello admin!"."<br />";
   echo "Password : ".$key;
  }else{
   echo "wrong..";
  }
 }
?>
<style>
 input[type=text] {width:200px;}
</style>
<br />
<br />
<form method="post" action="./index.php">
password : <input type="text" name="ps" /><input type="submit" value="login" />
</form>
<div><a href='?view-source'>get source</a></div>
```
-----
```php
 if(isset($_POST['ps'])){
  sleep(1);
  mysql_connect("localhost","md5_password","md5_password_pz");
  mysql_select_db("md5_password");
  mysql_query("set names utf8");
```
- post 방식으로 전달받은 ps의 값이 비어있지 않는지 확인하여 비어있으면 실행한다.

- mysql 서버에 연결하고 사용할 db를 고른다.
-----
```php
  $key=auth_code("md5 password");
  $ps = mysql_real_escape_string($_POST['ps']);
  $row=@mysql_fetch_array(mysql_query("select * from admin_password where password='".md5($ps,true)."'"));
  if(isset($row[0])){
   echo "hello admin!"."<br />";
   echo "Password : ".$key;
  }else{
   echo "wrong..";
```
- post로 받은 ps의 값중 특수문자를 이스케이프 처리한다.

- md5 함수로 바이너리로 암호화 하여 sql query를 완성시켜 mysql서버에 요청한다.

- 요청하여 리턴받은 데이터가 있을 경우 문제 풀이에 성공하며 flag를 출력한다

## 문제 해결 방안
md5() 함수의 두번째 인자로 true를 보낼경우 md5 암호화 결과가 바이너리 방식으로 암호화 된다.

sql injection으로 무조건 참이 되게끔 쿼리를 완성시켜 요청할경우 모든 데이터가 불러오기 때문에 문제 풀이에 성공한다.

암호화 결과가 1' or '1과 같은 문자열이 될 경우에 문제 풀이에 성공하는데 이런 결과를 만들 수 있는 문자열중 하나가 `129581926211651571912466741651878684928`이다. 이 문자열을 바이너리로 암호화할 경우 1' or '1 이 되어 쿼리를 완성시켜준다.

해당 문자열을 입력하여 나온 flag를 auth에 입력하면 문제풀이에 성공한다.