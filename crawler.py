#!/usr/bin/env python


import requests

def request(url):
    try:
        get_response = requests.get("http://" + url)
        print(get_response)
    except requests.exceptions.ConnectionError:
        pass

target_url = "Atanasfit.com"

with open("/usr/share/amass/wordlists/subdomains-top1mil-5000.txt", "r") as wordlist_file:  #r for read only
    for line in wordlist_file:
        word = line.strip()
        test_url = word + "." + target_url
        #print(test_url)
        response = request(test_url)
        if response:
            print("[+]OP -->" + test_url)

