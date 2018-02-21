# Wargame.kr No.13 - simple board

## 문제 출제 의도
board의 구조를 알고 SQL injection을 시도할줄 아는지 확인한다.

## 문제 이해
문제에 접근하기 전 힌트로써 `Simple Union SQL injection Challenge. (but you need script... maybe?)`가 출력되었다.

아무리 문제에 접근해보아도 어떻게 접근해야하는지 생각이 나질 않아 힌트를 둘러보았더니 SQL Injection문제이고 script가 필요할 것이라고 하였다.

다시 문제에 접근하니 보드가 출력되고 소스코드를 볼 수 있는 창이 출력되었었다.

```php
<?php
    if (isset($_GET['view-source'])){
        if (array_pop(split("/",$_SERVER['SCRIPT_NAME'])) == "classes.php") {
            show_source(__FILE__);
            exit();
        }
    }

    Class DB {
        private $connector;

        function __construct(){
            $this->connector = mysql_connect("localhost", "SimpleBoard", "SimpleBoard_pz");
            mysql_select_db("SimpleBoard", $this->connector);
        }

        public function get_query($query){
            $result = $this->real_query($query);
            return mysql_fetch_assoc($result);
        }

        public function gets_query($query){
            $rows = [];
            $result = $this->real_query($query);
            while ($row = mysql_fetch_assoc($result)) {
                array_push($rows, $row);
            }
            return $rows;
        }

        public function just_query($query){
            return $this->real_query($query);
        }

        private function real_query($query){
            if (!$result = mysql_query($query, $this->connector)) {
                die("query error");
            }
            return $result;
        }

    }

    Class Board {
        private $db;
        private $table;

        function __construct($table){
            $this->db = new DB();
            $this->table = $table;
        }

        public function read($idx){
            $idx = mysql_real_escape_string($idx);
            if ($this->read_chk($idx) == false){
                $this->inc_hit($idx);
            }
            return $this->db->get_query("select * from {$this->table} where idx=$idx");
        }

        private function read_chk($idx){
            if(strpos($_COOKIE['view'], "/".$idx) !== false) {
                return true;
            } else {
                return false;
            }
        }

        private function inc_hit($idx){
            $this->db->just_query("update {$this->table} set hit = hit+1 where idx=$idx");
            $view = $_COOKIE['view'] . "/" . $idx;
            setcookie("view", $view, time()+3600, "/SimpleBoard/");
        }

        public function get_list(){
            $sql = "select * from {$this->table} order by idx desc limit 0,10";
            $list = $this->db->gets_query($sql);
            return $list;
        }

    }
```
- 코드를 클래스로 나누어 작성한 것을 출력해 주었다.

- 위 코드를 보아 query문을 조작하는 부분은 select와 update로 이루어져있었다.
-----
보드에서 글을 눌러보니 hit가 증가하고 ?idx=보드 번호가 url에서 get방식으로 전달되고 있었으며 해당 sql이 cookie에 저장되고 있었다.

그래서 idx의 값을 5로 전달했더니 보드가 출력되지 않는 것을 보아 게시글의 갯수는 4개 인것을 알 수 있었다.

## 문제 해결 방안
idx 입력을 할 때 injection을 시도해 볼 수 있었으며 쿠키와 url을 모두 조작해야하기에 스크립트 언어를 사용하는 것이 편할 꺼라고 생각했고 그래서 사용한 스크립트 언어는 python이였다.

DATABASE의 정보를 사용하기위하여 information_schema.tables를 사용하였다.

`./src/simpleboard.py`코드를 실행하게 되면 base table을 찾게 되는데 simpleboard와 readme 테이블이 있는것을 보아 readme 테이블에 flag가 있음을 추측할 수 있었다.

quote를 필터링 하는 것 같아 str함수를 헥사코드로 다음과 같이 입력해 column_name을 알 수 있었다.
`5 union select culumn_name, data_type, 3, table_name from information_schema.columns where table_name = 0x524541444d45#`

위를 get방식으로 전달할시에 flag라는 컬럼이 있음을 알 수 있어 url에 다시 flag 컬럼을 찾는 sql 문을 다음과 같이 입력해보았다.
`5 union select flag, 2, 3, 4 from README#`를 입력하였더니 flag가 출력되었다.

해당 flag를 auth에 입력할 경우 문제풀이에 성공한다.