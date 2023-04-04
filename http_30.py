# In this challenge, your goal is to send a request to /pentesterlab using HTTP multipart, with a file using the parameter name: filename.
# The filename must contain a directory traversal (../).
# However, there is an option to prevent this behaviour (and it's different from the one used in http_25).
# This type of request is extremely useful when testing application with multiple layers of reverse proxies.

# curl http://ptl-2d40baca-22ba7e48.libcurl.so/pentesterlab -F 'filename=@test.txt;filename=../../test.txt'

import requests

url = 'http://ptl-2d40baca-22ba7e48.libcurl.so/pentesterlab'

# specify the data parameter as a dictionary with the directory traversal filename
files = {'filename': ('../../test.txt', open('test.txt', 'rb'))}

# send the request using the post method
r = requests.post(url, files=files)

print(r.url)
print(r.text)