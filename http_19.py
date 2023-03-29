# In this challenge, your goal is to send a GET request to /pentesterlab with the following GET` parameter: key as an array with the first element with the value key and the second element with the value please

# To send a parameter as an array, you can use the following syntax: name[0]=value1&name[1]=value2.

import requests

url = 'http://ptl-d87f2f26-b2168624.libcurl.so/pentesterlab'

# requests encodes the percentage by default
payload = {'key[0]' : 'key', 'key[1]' : 'please'}

r = requests.get(url, params=payload)

print(r.url)
print(r.text)