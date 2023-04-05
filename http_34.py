# In this challenge, your goal is to send a POST request to /pentesterlab with the body of the request containing the following XML:
# <key><value>[VALUE]</value></key>
# where [VALUE] should be replaced with <please>. The request should also set the header Content-Type to application/xml.

import requests

url = 'http://ptl-0d1f2233-3210da8a.libcurl.so/pentesterlab'

headers = {'Content-Type' : 'application/xml'}

files = {'file':'<key><value>&lt;please&gt;</value></key>'}

# send the request using the post method
r = requests.post(url, headers=headers, files=files)

print(r.url)
print(r.text)