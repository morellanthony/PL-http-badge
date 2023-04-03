# In this challenge, your goal is to send a request to /pentesterlab using HTTP multipart.

import requests

url = 'http://ptl-c755c70f-1bb823f6.libcurl.so/pentesterlab'

# open and read the bytes of a file in the current directory.
files = {'file': open('test.txt', 'rb')}

r = requests.get(url, files=files)

print(r.url)
print(r.text)
