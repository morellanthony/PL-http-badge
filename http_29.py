# In this challenge, your goal is to send a request to /pentesterlab using HTTP multipart with a file (at least one byte in size) using the parameter name: filename.

import requests

url = 'http://ptl-8aa74d58-04004ef5.libcurl.so/pentesterlab'

# open and read the bytes of a file in the current directory.
files = {'filename': open('test.txt', 'rb')}

r = requests.get(url, files=files)

print(r.url)
print(r.text)
