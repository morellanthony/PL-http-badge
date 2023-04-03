# In this challenge, your goal is to send a GET request to /pentesterlab/../pentesterlab.

import requests

url = 'http://ptl-d8ff6d6f-39d8a515.libcurl.so/pentesterlab/..%2Fpentesterlab'

r = requests.get(url)

print(r.url)
print(r.text)
