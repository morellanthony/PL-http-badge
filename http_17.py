# In this challenge, your goal is to send a GET request to /pentesterlab with the following GET parameter: key with the value please followed by a NULL Byte

import requests

url = 'http://ptl-5e0f98c4-dc08bd87.libcurl.so/pentesterlab?key=please%00'

r = requests.get(url)

print(r.url)
print(r.text)