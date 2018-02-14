# Wargame.kr No.06 - db is really good

## 문제 출제 의도
어떤 데이터베이스로 이루어져있는지 확인하고, 어떠한 관계로 유저와 데이터 베이스가 이루어져 있는지 확인한다.

## 문제 이해
문제에 접근하기 전에 힌트를 보면 `What kind of this Database? you have to find correlation between user name and database.`라며 데이터 베이스가 어떤 것인지 확인하고 유저 이름과 데이터베이스 관의 상호관계를 파악하라는 내용이였다.

그리고 문제에 접근하게 되면 user 이름을 입력하여 로그인을 할수 있는 입력창과 입력하여 로그인을 한 후에는 메모를 입력할 수 있는 input이  출력된다. 입력하여 메모를 등록해 내면 아래에 해당 메모가 출력된다.

## 문제 해결 방안
우선 admin으로 로그인하면 무엇이던 나올까 입력해보았지만 `dont access with 'admin'`가 출력된다. 

위를 보아 대충 admin에 접근해보자 하였다.

하지만 어떤 데이터 베이스인지 알아보기 위하여 우선 에러를 발생시켜보려고 하였다. 

여러 특수 문자를 입력해보았지만 /에서 에러가 출력되었고 데이터베이스가 SQLite3라는 것을 알 수 있었고 에러 문구 안에 `open('./db/wkrm_/.db')`를 볼 수 있었다. 

혹시나 db가 wkrm_유저네임.db 이런 구조로 이루어져 있나 에러를 다시 발생시키기 위하여 /를 입력하되 다른 문자를 섞어 */를 입력해보았다.

그랬더니 역시 `open('./db/wkrm_*/.db')`가 출력되어 wkrm_유저네임.db로 이루어져 있다고 판단하여 admin에 해당하는 db는 wkrm_admin.db라고 판단하였다.

따라서 URL에 `http://wargame.kr:8080/db_is_really_good/db/wkrm_admin.db`를 입력하였더니 해당 db를 다운받을 수 있었는데 SQLite3 방식이기 때문에 SQLite viewer 같은 프로그램을 이용해 살펴보아도 되지만 본인은 메모장을 이용하였다.

메모장으로 실행할 시에 특정 URL을 출력해주어 해당 URL을 다시 입력하니 flag를 출력해주었고 해당 flag를 auth에 입력하니 문제 풀이에 성공하였다.