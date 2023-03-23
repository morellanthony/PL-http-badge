# In this challenge, your goal is to send a POST request to /pentesterlab 
# with the following POST parameter: key with the value please

import requests

url = 'http://ptl-d0c0a603-1f410f14.libcurl.so/pentesterlab'

# Here I create a custom header as the payload.
payload = {'key': 'please'}

# Set the 'headers' value as the payload.
r = requests.post(url, data=payload)

print(r.url)
print(r.text)
