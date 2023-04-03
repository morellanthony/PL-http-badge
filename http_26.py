# In this challenge, your goal is to send a GET request to /pentesterlab;pentesterlab.

import requests

url = 'http://ptl-42c67eb7-dde4cdcd.libcurl.so/pentesterlab%3Bpentesterlab'

r = requests.get(url)

print(r.url)
print(r.text)
