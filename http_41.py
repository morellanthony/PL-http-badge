# In this challenge, your goal is to send a POST request to /pentesterlab with the body of the request containing the following YAML: key as an array with two values: please and please2. The request should also set the header Content-Type to application/yaml.

import requests

url = 'http://ptl-65db4c8a-8ccea47f.libcurl.so/pentesterlab'

headers = {'Content-Type' : 'application/yaml'}

payload = {'key':['please', 'please2']}

r = requests.post(url, headers=headers, json=payload)

print(r.url)
print(r.text)