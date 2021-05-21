### server.py #### 

import socket

s = socket.socket()
host = socket.gethostname()
port = 3000 # port(포트) : 통신 통로
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(5)
sw = None

while True:
    
    if sw is None:
        print( '[ 연결 대기... ] ')
        sw, addr = s.accept()
        print( ' 연결합니다 : ', addr)
 
    else:
        print( ' client : ', end = ' ')
        print((sw.recv(1024)).decode('utf-8'))
        msg = input(' Me : ')
        sw.send(msg.encode('utf-8'))

