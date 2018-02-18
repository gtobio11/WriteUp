# Wargame.kr No.08 - md5 compare

## 문제 출제 의도
php 매직 해쉬를 알고 있는지 확인하고 md5로 매직 해쉬에 접근할 수 있는지 확인한다.

## 문제 이해
문제에 접근하기 전의 힌트에 `JUST COMPARE ONLY.   with the other value :D`가 출력되었다.

문제에 접근하면 입력할 수 있는 창이 두개 출력되고 chk 버튼이 출력된다. 그리고 소스코드를 보게 해줄 a태그로써 `view-source`가 출력된다.

소스코드는 아래와 같다.

```php
<?php
    if (isset($_GET['view-source'])) {
         show_source(__FILE__);
         exit();
    }

    if (isset($_GET['v1']) && isset($_GET['v2'])) {
        sleep(3); // anti brute force

        $chk = true;
        $v1 = $_GET['v1'];
        $v2 = $_GET['v2'];

        if (!ctype_alpha($v1)) {$chk = false;}
        if (!is_numeric($v2) ) {$chk = false;}
        if (md5($v1) != md5($v2)) {$chk = false;}

        if ($chk){
            include("../lib.php");
            echo "Congratulations! FLAG is : ".auth_code("md5_compare");
        } else {
            echo "Wrong...";
        }
    }
?>
<br />
<form method="GET">
    VALUE 1 : <input type="text" name="v1" /><br />
    VALUE 2 : <input type="text" name="v2" /><br />
    <input type="submit" value="chk" />
</form>
<br />
<a href="?view-source">view-source</a>
```
-----
```php
    if (isset($_GET['v1']) && isset($_GET['v2'])) {
        sleep(3); // anti brute force

        $chk = true;
        $v1 = $_GET['v1'];
        $v2 = $_GET['v2'];

        if (!ctype_alpha($v1)) {$chk = false;}
        if (!is_numeric($v2) ) {$chk = false;}
        if (md5($v1) != md5($v2)) {$chk = false;}
```
- v1과 v2가 모두 입력되었는지 확인한다.

- v1 변수에 get방식으로 받아온 v1의 값을 담는다.

- v2 변수에 get방식으로 받아온 v2의 값을 담는다.

- v1 변수가 모두 영어로 이루어져있는지 확인한 후 아닐경우에 chk 변수를 false로 바꾼다.

- v2 변수가 모두 숫자로 이루어져있는지 확인한 후 아닐경우에 chk 변수를 false로 바꾼다.

- v1 변수와 v2 변수를 md5로 암호화한후에 값이 같은지 확인한 후에 아닐 경우 chk 변수를 false로 바꾼다.
-----
```php
        if ($chk){
            include("../lib.php");
            echo "Congratulations! FLAG is : ".auth_code("md5_compare");
        } else {
            echo "Wrong...";
        }
```
- chk의 값이 false가 아닐 경우  Congratulations! 가 출력되며 flag를 출력해준다.

- 아닐경우 Wrong...이 출력되며 문제 풀이에 실패한다.

## 문제 해결 방안
php 매직 해쉬를 이용하여 문제를 해결한다.

php의 경우 == 연산자로 비교를 할 경우 데이터 자료형과는 상관없이 값만 비교하게 되는데 0e로 시작할 경우 실수로 취급하여 계산한다.

0e의 경우 (a)e(b)과 같이 이루어져있는데 a의 10의 b승 이라는 의미를 가지고 있다. 이때 0e로 시작하게 되면 어떤 수라고 하던 1이 되기 때문에 어떠한 수라고 하더라도 0e로 시작할 경우에 == 연산자로 비교할경우 참을 리턴한다

md5로 암호화 하여 비교하기 때문에 암호화 하였을때 0e로 시작하는 숫자와 0e로 시작하는 문자열을 입력하게 되면 암호화 하면서 0e로 시작하게 되고 참을 리턴하여 문제 풀이에 성공할 수 있다.

이때 매직 해쉬에 해당하는 문자열과 숫자는 `QNKCDZO`와 `240610708`이 있다.

해당 숫자와 문자열을 입력할 경우 flag가 출력되며 해당 flag를 auth에 입력할 경우 문제 풀이에 성공한다.