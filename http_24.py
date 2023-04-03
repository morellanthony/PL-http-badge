# In this challenge, your goal is to send a request with the header X-Forwarded-Host set to pentesterlab.com to /pentesterlab.

import requests

# Custom header
headers = {'X-Forwarded-Host' : 'pentesterlab.com'}

url = 'http://ptl-77778d05-7f3da40e.libcurl.so/pentesterlab'

r = requests.get(url, headers=headers)

print(r.url)
print(r.text)
