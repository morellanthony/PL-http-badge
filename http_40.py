# In this challenge, your goal is to send a POST request to /pentesterlab with the body of the request containing the following YAML: key: please
# The request should also set the header Content-Type to application/yaml.

import requests

url = 'http://ptl-a1635604-56355014.libcurl.so/pentesterlab'

headers = {'Content-Type' : 'application/yaml'}

payload = {'key':'please'}

r = requests.post(url, headers=headers, json=payload)

print(r.url)
print(r.text)