# In this challenge, your goal is to send a request with the method HACK to /pentesterlab

import requests

# Extending the requests library to add a custom request type.
class MySession(requests.Session):
    def hack(self, url, **kwargs):
        
        # Sends a HACK request to the specified URL using the current session.
        
        return self.request('HACK', url, **kwargs)

url = 'http://ptl-4adda817-c9fffd40.libcurl.so/pentesterlab'

s = MySession()

r = s.hack(url)

print(r.url)
print(r.text)
