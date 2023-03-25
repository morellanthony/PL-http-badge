# In this challenge, your goal is to send a GET request to /pentesterlab with the following POST parameter: key with the value please

import requests

url = 'http://ptl-f9a4d24b-ed901c72.libcurl.so/pentesterlab'

payload = {'key':'please'}

# Set the request type to get and field parameter to data.
r = requests.get(url, data=payload)

print(r.url)
print(r.text)
