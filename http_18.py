# In this challenge, your goal is to send a GET request to /pentesterlab with the following GET parameter: key with the value please followed by a double-encoded NULL Byte

import requests

url = 'http://ptl-227c3965-2ed20fa8.libcurl.so/pentesterlab'

# requests encodes the percentage by default
payload = {'key' : 'please%00'}

r = requests.get(url, params=payload)

print(r.url)
print(r.text)