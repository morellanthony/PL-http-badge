# In this challenge, your goal is to connect to the websocket /pentesterlab and send the string key.
# Proxy Error

import socket

url = 'ws://ptl-876c5c19-ea4b4de8.libcurl.so/pentesterlab'
port = 80

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((url, port))
    s.sendall(b'key')
    data = s.recv(1024)

print(f"Received {data!r}")