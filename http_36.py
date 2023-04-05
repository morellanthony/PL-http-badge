# In this challenge, your goal is to send a POST request to /pentesterlab with the body of the request containing the following XML:
# <key value="please"></key>
# The request should also set the header Content-Type to application/xml.

import requests

url = 'http://ptl-5b0276f6-2ee080fa.libcurl.so/pentesterlab'

headers = {'Content-Type' : 'application/xml'}

files = {'file':'<key value="please"></key>'}

# send the request using the post method
r = requests.post(url, headers=headers, files=files)

print(r.url)
print(r.text)