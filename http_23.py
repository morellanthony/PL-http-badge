# In this challenge, your goal is to send a request with the header X-Forwarded-For set to 1.2.3.4 to /pentesterlab.

import requests

# Custom header
headers = {'X-Forwarded-For' : '1.2.3.4'}

url = 'http://ptl-be4142e6-e1a4e532.libcurl.so/pentesterlab'

r = requests.get(url, headers=headers)

print(r.url)
print(r.text)
