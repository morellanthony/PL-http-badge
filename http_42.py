# In this challenge, your goal is to send a GET request to /pentesterlab with an authentication Basic with the username key and the password please.

import requests
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('key', 'please')

url = 'http://ptl-6f96e378-e37a969c.libcurl.so/pentesterlab'

r = requests.get(url, auth=auth)

print(r.url)
print(r.text)