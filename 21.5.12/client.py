#client.py

import socket

s = socket.socket()
host = socket.gethostname()
port = 3000 # port(포트) : 통신 통로
s.connect((host, port))
print( ' 연결합니다 : ', host)

while True:
    
    msg = input(' Me : ')
    s.send(msg.encode('utf-8'))

    print(' server : ', end = ' ')
    print((s.recv(1024)).decode('utf-8'))
