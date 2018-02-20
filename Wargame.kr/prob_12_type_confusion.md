# Wargame.kr No.12 - type confusion

## 문제 출제 의도
JSON 형식의 데이터 형식을 알고 패킷을 조작하여 전송할 수 있는지 확인한다.

## 문제 이해
문제에 접근하기전 힌트에 `Simple Compare Challenge.  hint? you can see the title of this challenge. :D`가 출력된다

문제에 접근하면 key를 입력할 수 있는 창과 check 버튼, 소스코드를 볼 수 있는 링크가 출력된다.

아래는 해당 소스코드이다.
```php
<?php
 if (isset($_GET['view-source'])) {
     show_source(__FILE__);
    exit();
 }
 if (isset($_POST['json'])) {
     usleep(500000);
     require("../lib.php"); // include for auth_code function.
    $json = json_decode($_POST['json']);
    $key = gen_key();
    if ($json->key == $key) {
        $ret = ["code" => true, "flag" => auth_code("type confusion")];
    } else {
        $ret = ["code" => false];
    }
    die(json_encode($ret));
 }

 function gen_key(){
     $key = uniqid("welcome to wargame.kr!_", true);
    $key = sha1($key);
     return $key;
 }
?>

<html>
    <head>
        <script src="//ajax.googleapis.com/ajax/libs/jquery/1.8.1/jquery.min.js"></script>
        <script src="./util.js"></script>
    </head>
    <body>
        <form onsubmit="return submit_check(this);">
            <input type="text" name="key" />
            <input type="submit" value="check" />
        </form>
        <a href="./?view-source">view-source</a>
    </body>
</html>
```
-----
```php
 if (isset($_POST['json'])) {
     usleep(500000);
     require("../lib.php"); // include for auth_code function.
    $json = json_decode($_POST['json']);
    $key = gen_key();
```
- POST 방식으로 받은 json이 비어있는지 확인한다.

- POST 방식으로 받은 json을 JSON 방식으로 인코딩 되어있는 것을 복호화시킨다.

- gen_key() 함수를 실행시켜 키값을 리턴 받아 $key 변수에 답는다.
-----
```php
if ($json->key == $key) {
        $ret = ["code" => true, "flag" => auth_code("type confusion")];
    } else {
        $ret = ["code" => false];
    }
```
- 복호화한 json의 key값이 리턴받은 키값과 같은지 확인하여 맞다면 $ret 변수에 code는 true와 flag를 담는다.

- 아니라면 code를 false로 $ret 변수에 담는다.
-----
```php
    die(json_encode($ret));
```
- $ret를 json 방식으로 인코딩 시켜 출력시키며 끝낸다.
-----
```php
function gen_key(){
    $key = uniqid("welcome to wargame.kr!_", true);
    $key = sha1($key);
    return $key;
}
```
- uniqid와 sha1방식을 이용하여 키를 생성하여 리턴한다.

## 문제 해결 방안
key값은 비어있지 않기 때문에 == 비교를 할때 불리언값과 비교를 한다면 항상 true값을 갖는다.

따라서 json을 인코딩한 것의 key값이 true라면 문제 풀이에 성공한다.

필자는 burp suite를 문제를 풀기위해 사용하였다.

어느 값이든 입력하고 패킷을 보내고 그것을 burp suite로 intercept하여 확인하여 보면 key값이 json방식로 인코딩 되어있는 것을 볼 수 있었다.

그 패킷의 code값을 수정하여 true로 바꾸어 준다면 if문 비교에 true로 적용되면서 flag를 출력하고 해당 flag를 auth에 입력하면 문제풀이에 성공한다.