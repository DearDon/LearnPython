#This version can be more interactive to output a form,
#and get input by POST method
import socket

HOST=''
PORT=8000

text_content= '''
HTTP/1.X 200 OK
Content-Type: text/html

<head>
<title>WOW</title>
</head>
<html>
<p>Wow, Python Server</p>
<IMG src="test.jpg"/>
<form name="imput" action="/" method="post">
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

#Configure socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST, PORT))

# Serve forever
while True:
	s.listen(3)
	conn, addr=s.accept()
	request=conn.recv(1024)
	method=request.split(' ')[0]
	src=request.split(' ')[1]

	print 'Connected by', addr
	print 'Reguest is:', request

	# if GET method request
	if method =='GET':
		if src=='/test.jpg':
			content=pic_content
		else:
			content=text_content
		#send message
		conn.sendall(content)
	
	# if POST method request
	if method=='POST':
		form=request.split('\r\n')
		idx=form.index('')
		entry=form[idx:]

		value=entry[-1].split('=')[-1]
		conn.sendall(text_content + '\n<p>' + value + '</p>')

		#####
		# More operations

		######
	# close connection
	conn.close()

