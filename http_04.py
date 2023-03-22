# In this challenge, your goal is to send a GET request to /pentesterlab with the Content-Type set to key/please

import requests

url = 'http://ptl-b13d0d5f-af66c033.libcurl.so/pentesterlab'

# Here I create a custom header as the payload.
payload = {'content-type': 'key/please'}

# Set the 'headers' value as the payload.
r = requests.get(url, headers=payload)

print(r.url)
print(r.text)
