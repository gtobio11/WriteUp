# Wargame.kr No.11 - strcmp

## 문제 출제의도
strcmp 함수의 취약점을 알고 패킷을 조작하여 문제가 원하는 바에 이룰수 있는지 확인한다.

## 문제 이해
문제에 접근하기 전 힌트에서 `if you can bypass the strcmp function, you get the flag.`를 출력한다.

문제에 접근하면 password를 입력할 수 있는 창과 chk버튼, 소스코드를 볼수 있는 링크가 출력된다.

아래는 해당 소스코드이다.
```php
<?php
    require("../lib.php"); // for auth_code function

    $password = sha1(md5(rand().file_get_contents("/var/lib/dummy_file")).rand());

    if (isset($_GET['view-source'])) {
        show_source(__FILE__);
        exit();
    }else if(isset($_POST['password'])){
        sleep(1); // do not brute force!
        if (strcmp($_POST['password'], $password) == 0) {
            echo "Congratulations! Flag is <b>" . auth_code("strcmp") ."</b>";
            exit();
        } else {
            echo "Wrong password..";
        }
    }

?>
<br />
<br />
<form method="POST">
    password : <input type="text" name="password" /> <input type="submit" value="chk">
</form>
<br />
<a href="?view-source">view-source</a>
```
-----
```php
$password = sha1(md5(rand().file_get_contents("/var/lib/dummy_file")).rand());
```
- rand()함수의 리턴값과 `/var/lib/dummy_file`파일의 내용으로 md5암호화 한후 그 값과 rand()함수의 리턴값 더해서 sha1방식으로 암호화 하여 password를 만들어 $password변수에 담는다.

-----
```php
if (isset($_GET['view-source'])) {
    show_source(__FILE__);
    exit();
}else if(isset($_POST['password'])){
    sleep(1); // do not brute force!
    if (strcmp($_POST['password'], $password) == 0) {
        echo "Congratulations! Flag is <b>" . auth_code("strcmp") ."</b>";
        exit();
    } else {
        echo "Wrong password..";
    }
}
```
- view-source가 GET방식으로 전달되면 소스코드를 보여준다.

- POST 방식으로 password를 전달한 값이 빈값이 아니면 실행한다.

- strcmp함수로 POST 방식으로 전달 받은 password과 $password변수의 값을 비교하여 리턴된 값과 0 과 비교하여 참이라면 flag를 출력하고 아니라면 문제풀이에 실패한다.

## 문제 해결방안
strcmp함수의 취약점을 이용한다.

strcmp함수는 인자로써 넘겨온 값중 배열이 있으면 0을 리턴한다.

password 문자열 방식으로 전달되고 있는데 이 패킷을 수정하여 배열로 보낸다면 문제가 원하는 바에 이룰 수 있을 것같다.

패킷에 password는 `password=입력값` 이렇게 전달되는데 패킷을 수정하여 `password[]=아무값`을 하게 된다면 flag를 출력하며 해당 flag를 auth에 입력하게 되면 문제 풀이에 성공한다. 