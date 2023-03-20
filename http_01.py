# In this challenge, your goal is to send a GET request to /pentesterlab

import requests

url = 'http://ptl-ca986611-4e04302e.libcurl.so/pentesterlab'

r = requests.get(url)

print(r.status_code)
print(r.text)