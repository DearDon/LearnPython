#This version's function is just like the v2, but use package SocketServer instead of Socket
import SocketServer

HOST=''
PORT=8000

text_content='''
HTTP/1.x 200 OK
Content-Type: text/html

<head>
<title>WOW</title>
</head>
<html>
<p>Wow, Python Server</p>
<IMG src="test.jpg"/>
<form name="input" action="/" method="post">
First name:<input type="text" name="firstname"><br>
<input type="submit" value="Submit">
</form>
</html>
'''

f=open('test.jpg','rb')
pic_content='''
HTTP/1.x 200 OK
Content-Type: image/jpg

'''
pic_content=pic_content+f.read()

#This class defines response to each request
class MyTCPHandler(socketServer.BaseRequstHandler):
	def handler(self):
		request=self.request.recv(1024)
		print 'connected by', self.client_address[0]
		print 'Request is', request

		method=request.split(' ')[0]
		src=request.split(' ')[1]

		if method='GET'
			if src=='/test.jpg':
				content=pic_content
			else:
				content=text_content
			self.request.sendall(content)

		if method=='POST':
			form=request.split('\r\n')
			idx=form.index('')
			entry=form[idx:]

			value=entry[-1].split('=')[-1]
			self.request.sendall(text_content+'\n<p>'+value+'</p>')
			#####
			#More operations
			####

# Create the server
server=SocketServer.TCPServer((HOST, PORT),MyTCPHandler)
# Start the server
server.serve_forever()
