# In this challenge, your goal is to send a GET request to /pentesterlab#pentesterlab.

import requests

url = 'http://ptl-716075ed-7f7d04ba.libcurl.so/pentesterlab%23pentesterlab'

r = requests.get(url)

print(r.url)
print(r.text)
