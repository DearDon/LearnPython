#This version only response to a client simple words
import socket

#Address
HOST=''
PORT=8000

reply='Yes'

#configure
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))


s.listen(3)

conn,addr=s.accept()

request=conn.recv(1024)

print('request is:',request)
print('Connected by',addr)

conn.sendall(reply)
conn.close()
