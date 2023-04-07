# In this challenge, your goal is to send a POST request to /pentesterlab with the body of the request containing the following JSON: {"key": "please"} The request should also set the header Content-Type to application/json.

import requests

url = 'http://ptl-3384fd2a-1e10a520.libcurl.so/pentesterlab'

headers = {'Content-Type' : 'application/json'}

payload = {'key':'please'}

r = requests.post(url, headers=headers, json=payload)

print(r.url)
print(r.text)