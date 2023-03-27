# In this challenge, your goal is to send a POST request to /pentesterlab 
# with the following GET parameter key with the value please and the following POST parameter key with the value please

import requests

url = 'http://ptl-334fa3eb-17efbcf2.libcurl.so/pentesterlab'

payload = {'key': 'please'}

# Using a post request send post data and get parameters in the same request.
r = requests.post(url, data=payload, params=payload)

print(r.url)
print(r.text)
