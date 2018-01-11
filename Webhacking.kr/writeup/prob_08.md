# Webhacking.kr No.08

## 문제 출제 의도
코드를 분석하여 SQL문을 Injection을 통해 조작할 수 있는지 파악한다.

## 소스 코드 분석
```php
 <html>
<head>
<title>Challenge 8</title>
<style type="text/css">
body { background:black; color:white; font-size:10pt; }
</style>
</head>
<body>
<br><br>
<center>USER-AGENT

<?

$agent=getenv("HTTP_USER_AGENT");
$ip=$_SERVER[REMOTE_ADDR];

$agent=trim($agent);

$agent=str_replace(".","_",$agent);
$agent=str_replace("/","_",$agent);

$pat="/\/|\*|union|char|ascii|select|out|infor|schema|columns|sub|-|\+|\||!|update|del|drop|from|where|order|by|asc|desc|lv|board|\([0-9]|sys|pass|\.|like|and|\'\'|sub/";

$agent=strtolower($agent);

if(preg_match($pat,$agent)) exit("Access Denied!");

$_SERVER[HTTP_USER_AGENT]=str_replace("'","",$_SERVER[HTTP_USER_AGENT]);
$_SERVER[HTTP_USER_AGENT]=str_replace("\"","",$_SERVER[HTTP_USER_AGENT]);

$count_ck=@mysql_fetch_array(mysql_query("select count(id) from lv0"));
if($count_ck[0]>=70) { @mysql_query("delete from lv0"); }


$q=@mysql_query("select id from lv0 where agent='$_SERVER[HTTP_USER_AGENT]'");

$ck=@mysql_fetch_array($q);

if($ck)
{ 
echo("hi <b>$ck[0]</b><p>");
if($ck[0]=="admin")

{
@solve();
@mysql_query("delete from lv0");
}


}

if(!$ck)
{
$q=@mysql_query("insert into lv0(agent,ip,id) values('$agent','$ip','guest')") or die("query error");
echo("<br><br>done!  ($count_ck[0]/70)");
}


?>

<!--

index.phps

-->

</body>
</html>
 
```
* USER_AGENT 값을 받아와 변수 $agent에 담는다.

* 사이트 접속자의 IP값을 받아와 $ip에 담는다.

* $agent의 앞뒤 공백을 없앤후 각종 문자열을 필터링 해낸 후에 모두 소문자로 바꾼다.

* 사이트에 접속한 사용자의 브라우저 환경을 받아와 `'`,`"`를 공백으로 없애주어 브라우저 환경 정보를 수정한다.

* 설정한 $_SERVER[HTTP_USER_AGENT] 값으로 query를 날려서 결과를 q에 받아오고 mysql_fetch_array에 그 값을 저장하여 ck에 저장한다.

* 그 값이 admin이면 문제풀이에 성공하고 ck가 비어있다면 $agent,$ip값으로 guest로 db에 insert한다.

## 문제 해결 방안
mysql에서 insert할때 value값을 `,`로 구분하여 insert하면 구분된 두개 다 모두 insert 된다.

이를 이용하여 $agent값을 수정하여 injection해줄경우에 admin을 insert해주고 바꾼 agent값으로 요청을 해줄경우 문제풀이에 성공한다.

src폴더의 prob_08.py 파일은 위의 해결방안을 코드화 시킨것이다. 자신의 PHPSESSID를 입력하여주면 간단히 문제풀이에 성공한다.