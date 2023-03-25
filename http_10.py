# In this challenge, your goal is to send a GET request to /pentesterlab with the following GET parameter key twice. Both with the value please.

import requests

url = 'http://ptl-158c1a52-12b556f0.libcurl.so/pentesterlab'

# Two keys and two pleases in the payload. Used a dictionary here to pass the same data in the post request.
payload = {'key': ['please','please']}

# Set the request type to post and field parameter to data.
r = requests.post(url, data=payload)

print(r.url)
print(r.text)
