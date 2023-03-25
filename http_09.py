# In this challenge, your goal is to send a GET request to /pentesterlab with the following GET parameter key twice. Both with the value please.

import requests

url = 'https://ptl-313c82b3-1b19d580.libcurl.so/pentesterlab'

# Two keys and two pleases in the payload. Cannot use the same name in a key/value parameters, so I used a dictionary key.
payload = {'key': ['please','please']}

# Set the request type to get and field parameter to params.
r = requests.get(url, params=payload)

print(r.url)
print(r.text)
