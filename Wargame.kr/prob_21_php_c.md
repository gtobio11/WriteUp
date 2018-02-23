# Wargame.kr No.21 - php? C?

## 문제 출제 의도
C언어의 오버플로우를 이용하여 문제를 풀 수 있는지 확인하고 문제가 원하는 바를 이룰 수 있는지 확인한다.

## 문제 이해
문제에 접근하기전 힌트로써 `do you know "integer type" of 32bit application?`가 출력된다.

문제에 접근하게 되면 D1과 D2를 입력할 수 있는 창과 try 버튼이 출력되며 소스코드를 볼 수 있는 링크가 출력된다.

소스코드를 보면 아래와 같은 코드가 출력된다.
```php
<?php
 if (isset($_GET['view-source'])) {
     show_source(__FILE__);
    exit();
 }
 require("../lib.php"); // include for auth_code function.
 if(isset($_POST['d1']) && isset($_POST['d2'])){
  $input1=(int)$_POST['d1'];
  $input2=(int)$_POST['d2'];
  if(!is_file("/tmp/p7")){exec("gcc -o /tmp/p7 ./p7.c");}
  $result=exec("/tmp/p7 ".$input1);
  if($result!=1 && $result==$input2){echo auth_code("php? c?");}else{echo "try again!";}
 }else{echo ":p";}
?>
<style>
 table {background-color:#000; color:#fff;}
 td {background-color:#444;}
</style>
<hr />
 <center>
  <form method='post'>
  <table>
  <tr><td>D1:</td><td><input type='text' id="firstf" style="width:75px;" maxlength="9" name='d1'></td></tr>
  <tr><td>D2:</td><td><input type='text' style="width:75px;" name='d2'></td></tr>
  <tr><td colspan="2" style="text-align:center;"><input type='submit' value='try'></td></tr>
  </table>
  </form>
 <div><a href='?view-source'>get source</a></div>
 </center>
 <script>
  document.getElementById("firstf").focus();
 </script>
```
-----
```php
 if(isset($_POST['d1']) && isset($_POST['d2'])){
  $input1=(int)$_POST['d1'];
  $input2=(int)$_POST['d2'];
```
- POST 방식으로 보내는 d1과 d2가 모두 있는지 확인하여 존재할때 실행한다.

- POST 방식으로 전달받은 d1의 값을 int 자료형으로 캐스팅하여 $input1 변수에 담는다.

- POST 방식으로 전달받은 d2의 값을 int 자료형으로 캐스팅하여 $input2 변수에 담는다.
-----
```php
  if(!is_file("/tmp/p7")){exec("gcc -o /tmp/p7 ./p7.c");}
  $result=exec("/tmp/p7 ".$input1);
```
- 서버에 p7이라는 파일이 있는지 확인하고 없다면 p7.c파일을 컴파일 한다.

- p7파일을 실행시키는데 파라미터로 $input1 변수를 사용하고 리턴값을 $result 변수에 저장한다.
-----
```php
if($result!=1 && $result==$input2){echo auth_code("php? c?");}else{echo "try again!";}
```
- $result의 값이 1이 아니고 $result값과 $input2의 값이 같을때 auth_code의 인자로 "php? c?" 를 보내 리턴값을 출력한다.

- 아닐 경우 `try again!`을 출력한다.
---
다음은 p7.c에 해당하는 c언어 코드이다.
```c
#include <stdio.h>
#include <stdlib.h>
void nono();
int main(int argc,char **argv){
 int i;
 if(argc!=2){nono();}
 i=atoi(argv[1]);
 if(i<0){nono();}
 i=i+5;
 if(i>4){nono();}
 if(i<5){printf("%d",i);}
 return 0;
}
void nono(){
  printf("%d",1);
  exit(1);
}
```
- 인자로 넘어온 값이 2가 아니면 nono() 함수를 실행한다.

- argv[1]에 해당하는 값을 int 자료형으로 변환하여 i 변수에 저장한다.

- i가 0보다 작으면 nono() 함수를 실행한다.

- i를 5더한다.

- i가 4보다 크다면 nono() 함수를 실행한다.

- i가 5보다 작다면 i를 출력한다.

- 위에 조건에 아무것도 걸리지 않았다면 0을 리턴한다.

- nono 함수는 1를 출력하고 1을 리턴하며 종료시키는 함수이다.

## 문제 해결 방안
C언어의 int형 오버플로우를 이용하여 문제를 해결할 수 있다.

오버플로우가 발생할시에 해당 파일을 종료하는데 오버플로우를 난 값에 따라 음수 혹은 0이 리턴된다.

int형의 최댓값은 2147483647인데 c언어 내에서 5를 더하게 되므로 오버플로우가 발생된다.

2147483643에 5를 더하여 오버플로우가 발생될경우 int형의 최솟값인 -2147483648이 되므로 D1에 2147483643을 입력하고 D2에 -2147483648을 입력할 경우 D1과 D2는 같아지게 된다.

헌데 D1을 입력할 수 있는 input태그의 maxlength는 9이므로 2147483643를 모두 입력할 수 없어 개발자도구로 조작하여 입력하거나 패킷을 수정하여 문제를 풀 수 있다.

위의 두수를 입력하게 되면 flag를 출력하고 해당 flag를 auth에 입력할 경우 문제 풀이에 성공한다.