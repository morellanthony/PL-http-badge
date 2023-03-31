# In this challenge, your goal is to send a request with the header X-HTTP-Method-Override set to HACK to /pentesterlab.

import requests

# Custom header
headers = {'X-HTTP-Method-Override' : 'HACK'}

url = 'http://ptl-336e868b-16b3efe2.libcurl.so/pentesterlab'

r = requests.get(url, headers=headers)

print(r.url)
print(r.text)
