# In this challenge, your goal is to send a GET request to /pentesterlab with the following GET parameter: key with the value pretty please

import requests

url = 'http://ptl-884fea83-eda4d7ea.libcurl.so/pentesterlab'

payload = {'key' : 'pretty please'}

r = requests.get(url, params=payload)

print(r.url)
print(r.text)
