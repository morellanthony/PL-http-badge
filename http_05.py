# In this challenge, your goal is to send a GET request to /pentesterlab with the Accept-Language set to key-please

import requests

url = 'http://ptl-94af91fc-97ce22a2.libcurl.so/pentesterlab'

# Here I create a custom header as the payload.
payload = {'Accept-Language': 'key-please'}

# Set the 'headers' value as the payload.
r = requests.get(url, headers=payload)

print(r.url)
print(r.text)
