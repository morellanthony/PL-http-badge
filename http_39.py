# In this challenge, your goal is to send a POST request to /pentesterlab with the body of the request containing the following JSON: {"key": "[VALUE]"} with [VALUE] set to please". The request should also set the header Content-Type to application/json.

import requests

url = 'http://ptl-196e5ccd-04cc2ab5.libcurl.so/pentesterlab'

headers = {'Content-Type' : 'application/json'}

payload = {'key':'please\u0022'}

r = requests.post(url, headers=headers, json=payload)

print(r.url)
print(r.text)