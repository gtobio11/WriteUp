# Webhacking.kr No.32

## 문제 출제 의도
쿠키 값을 제외하고 요청하는 스크립트 코드를 작성할 수 있는지 확인한다.

## 문제 이해
문제에 접근하면 마치 랭킹 창과 같은 화면이 출력된다.

화면 최하단에 join 버튼이 있고 버튼을 누를 시에 도전자의 아이디와 클릭횟수가 화면에 출력된다.

마치 설문조사와 같이 버튼을 클릭할시 횟수가 증가한다.

한번 클릭하면 `vote_check`라는 쿠키가 생성되며 더이상 클릭할 때마다 no가 출력되며 숫자가 증가하지 않는다.

숫자가 100에 달할시에 문제풀이에 성공한다.

## 문제 풀이 방안
`vote_check`라는 쿠키를 삭제하고 다시한번 시도해봤을때 다시 투표가 가능했었다.

쿠키를 지우고 클릭하는 것을 반복하여 총 100번 누를시에 문제풀이에 성공하는데 직접 지우고 누르는 방법은 너무 번거로우므로 우선 python 코드를 작성해 보았다.

그 코드가 `../src/prob_32.py` 였는데 성공적으로 되지 않았다.

그래서 burp suite를 이용하여 문제를 푸는데에 시도해보았는데 burp suite의 send to repeat 을 이용하여 한 패킷을 여러번 전송시키는 것을 이용하여 100번 눌러 문제 풀이에 성공했다.