import urllib.request
from urllib.parse import quote

id = "gtobio11"
for i in range(1, 101):
    url = "http://webhacking.kr/challenge/codeing/code5.html?hit="
    data = "{}".format(id)
    print( str(i) + ": " + url + data)
    re = urllib.request.Request(url + data)
    re.add_header("User-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")
    re.add_header("Cookie", "PHPSESSID=a312bd37033d1ea94cb3776c5b8ec2a9")
print("Finshed !!!")