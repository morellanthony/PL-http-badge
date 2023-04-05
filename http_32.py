# In this challenge, your goal is to send a POST request to /pentesterlab with the body of the request containing:
# <key><value>please</value></key>
# and the header Content-Type set to application/xml.

import requests

url = 'http://ptl-dc37519e-8422755a.libcurl.so/pentesterlab'

headers = {'Content-Type' : 'application/xml'}

files = {'file':'<key><value>please</value></key>'}

# send the request using the post method
r = requests.post(url, headers=headers, files=files)

print(r.url)
print(r.text)