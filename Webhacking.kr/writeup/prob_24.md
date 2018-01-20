# Webhacking.kr No.24

## 문제 출제 의도
ip를 조작하여 str_replace 함수를 우회할 수 있는지 확인한다.

## 문제 이해
```php
<?

extract($_SERVER);
extract($_COOKIE);

if(!$REMOTE_ADDR) $REMOTE_ADDR=$_SERVER[REMOTE_ADDR];

$ip=$REMOTE_ADDR;
$agent=$HTTP_USER_AGENT;


if($_COOKIE[REMOTE_ADDR])
{
$ip=str_replace("12","",$ip);
$ip=str_replace("7.","",$ip);
$ip=str_replace("0.","",$ip);
}

echo("<table border=1><tr><td>client ip</td><td>$ip</td></tr><tr><td>agent</td><td>$agent</td></tr></table>");

if($ip=="127.0.0.1")
{
@solve();
}

else
{
echo("<p><hr><center>Wrong IP!</center><hr>");
}
?>
```
* index.phps에서 확인할 수 있는 코드이다.

* REMOTE_ADDR이 없을때 사용자의 ip를 받아 $ip 변수에 담아준다.

* 사용자의 브라우저 정보를 $agent 변수에 담아준다.

* $ip 변수의 `12`,`7.`,`0.`을 문자열에서 삭제한다.

* $ip 변수의 값이 `127.0.0.1`일때 문제 풀이에 성공한다.

## 문제 해결 방안
REMOTE_ADDR 쿠키를 만들어 그곳에 ip변수에 담고자 하는 값을 입력하면 된다.

str_replace 함수로 `12`,`7.`,`0.`을 문자열에서 삭제 하기 때문에 이 문자열을 우회해야한다.

* `12`의 경우 `1122`와 같이 입력하게 되면 가운데의 `12`가 문자열에서 삭제되면서 `12`만 남게 된다.

* `7.`의 경우 `77..`과 같이 입력하게 되면 가운데의 `7.`이 문자열에서 삭제되면서 `7.`만 남게 된다.

* `0.`의 경우 `00..`과 같이 입력하게 되면 가운데의 `0.`이 문자열에서 삭제되면서 `0.`만 남게 된다.

위의 세가지 방법을 사용하여 `112277..00..00..1`을 REMOTE_ADDR 쿠키에 입력하면 `127.0.0.1`이 남아 문제 풀이에 성공한다.