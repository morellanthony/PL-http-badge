# In this challenge, your goal is to send a POST request to /pentesterlab with an empty body.

import requests

url = 'http://ptl-6394a2c4-c62f1520.libcurl.so/pentesterlab'

# Set the request type to post and leave it empty.
r = requests.post(url)

print(r.url)
print(r.text)
