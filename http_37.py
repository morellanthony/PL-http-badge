# In this challenge, your goal is to send a POST request to /pentesterlab with the body of the request containing the following XML:
# <key value="[VALUE]"></key>
# with [VALUE] set to "please. The request should also set the header Content-Type to application/xml.

import requests

url = 'http://ptl-edba7b7a-b5d16561.libcurl.so/pentesterlab'

headers = {'Content-Type' : 'application/xml'}

files = {'file':'<key value="&quot;please"></key>'}

# send the request using the post method
r = requests.post(url, headers=headers, files=files)

print(r.url)
print(r.text)