# Wargame.kr No.05 - WTF CODE

## 문제 출제 의도
whitespace라는 언어를 아는지 확인하고 ws확장자를 읽을 수 있는지 확인한다.

## 문제 이해
문제에 접근하면 `이게 진짜 소스코드라고? 아무것도 안보인다고!!   is this source code really???? I can't see anything really!`가 출력되며 `source_code.ws`라는 코드를 다운 받을 수 있는 링크가 출력된다.

source_code.ws 파일을 다운 받고 에디터로 실행시켜보니 여러 공백으로 이루어진 소스가 출력된다.

해당 코드를 실행시키면 flag를 출력하는 것 같다.

## 문제 해결 방안
해당 소스코드를 실행시킬 수 있는 에디터나 환경을 맞추어 소스를 실행시키면 되는데 `https://ideone.com/` 이 URL에 접근하면 각종 언어의 환경을 웹 사이트로 구현시켜놓은 페이지로써 whitespace 언어를 실행시킬 수 있다.

다운 받은 소스코드를 위의 페이지에서 실행시키면 flag가 출력되고 해당 flag를 auth에 입력하면 문제풀이에 성공한다.