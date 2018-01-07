# Webhacking.kr No.01

## 문제 출제 의도
php 코드에 대한 이해와 쿠키를 조작할 수 있는지를 안다.

## 소스 코드 분석
```php
<?
if(!$_COOKIE[user_lv])
{
SetCookie("user_lv","1");
echo("<meta http_equiv=refresh content=0>")
}
?>
<html>
<head>
<title>Challenge 1</title>
</head>
<body bgcolor=black>
<center>
<br><br><br><br><br>
<font color=white>
---------------------<br>
<?
$password="????";
if(eregi("[^0-9,.]",$_COOKIE[user_lv])) $_COOKIE[user_lv]=1;
if($_COOKIE[user_lv]>=6) $_COOKIE[user_lv]=1;
if($_CCOKIE[user_lv]>5) @solve();
echo("<br>level : $_COOKIE[user_lv]")
?>
<br>
<pre>
<a onclick=location.href='index.phps'>----- index.phps -----</a>
</body>
</html>
```
-----
```php
if(!$_COOKIE[user_lv])
{
SetCookie("user_lv","1");
echo("<meta http_equiv=refresh content=0>")
}
```
* 만약 user_lv 라는 쿠키가 존재하지 않다면 user_lv라는 쿠키를 1값으로 만든다.
-----
```php
if(eregi("[^0-9,.]",$_COOKIE[user_lv])) $_COOKIE[user_lv]=1;
if($_COOKIE[user_lv]>=6) $_COOKIE[user_lv]=1;
if($_CCOKIE[user_lv]>5) @solve();
echo("<br>level : $_COOKIE[user_lv]")
```
* user_lv라는 쿠키 값이 0~9로 시작하는지 확인하여 시작하지 않는다면 user_lv 쿠키값을 1로 바꾼다.

* user_lv라는 쿠키 값이 6 이상이어도 값을 다시 1로 바꿔준다.

* user_lv라는 쿠키 값이 5 이상이면 답이 나온다.

## 문제 해결 방안
문제를 로드시에 만들어지는 user_lv 쿠키의 값을 5 초과 6미만의 값으로 바꾸어 주면 문제풀이에 성공한다.