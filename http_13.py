# In this challenge, your goal is to send a GET request to /pentesterlab with the following GET parameter: key with the value please&

import requests

url = 'http://ptl-f64c154e-2a99cb18.libcurl.so/pentesterlab'

payload = {'key' : 'please&'}

r = requests.get(url, params=payload)

print(r.url)
print(r.text)
