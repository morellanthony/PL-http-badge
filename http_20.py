# In this challenge, your goal is to send a GET request to /pentesterlab with the following GET parameter: key as a hash/dictionary with the key please set to 1

# To send the parameter as a hash/dictionary, you can use the following syntax: name[key]=value.

import requests

url = 'http://ptl-ac33a44c-9835948c.libcurl.so/pentesterlab'

payload = {'key[please]' : '1'}

r = requests.get(url, params=payload)

print(r.url)
print(r.text)
