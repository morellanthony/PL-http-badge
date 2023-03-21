# In this challenge, your goal is to send a GET request to /pentesterlab 
# with the following cookie: key with the value please

import requests

url = 'http://ptl-e084c9a2-4ae8b2ee.libcurl.so/pentesterlab'
cookies = dict(key='please')

r = requests.get(url, cookies=cookies)

print(r.url)
print(r.text)