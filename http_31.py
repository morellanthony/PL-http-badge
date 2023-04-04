# In this challenge, your goal is to send a POST request to /pentesterlab with the body of the request containing:

import requests

url = 'http://ptl-3841dc3f-f661f7b3.libcurl.so/pentesterlab'

files = {'file': ('test.txt', '<key><value>please</value></key>')}

# send the request using the post method
r = requests.post(url, files=files)

print(r.url)
print(r.text)