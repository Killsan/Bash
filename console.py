#!/usr/bin/python3

import os
import sys
import shutil
import socket

def autoincrement(var):
	files = os.listdir()
	for i in files:
		if var in i:
			return i 

def server(ip, user):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		sock.connect((ip, 8080))
	except ConnectionRefusedError:
		try:
			sock.connect((ip, 8000))
		except ConnectionRefusedError:
				try:
					sock.connect((ip, 8888))
				except ConnectionRefusedError:
					try:
						sock.connect((ip, 8008))
					except ConnectionRefusedError:
						print('Error')
	while True:
		command = input(user + ':~$ ')
		cmd = command.split()
		if cmd[0] == 'exit' or cmd[0] == 'quit':
			sock.send(b'exit')
			break
		sock.send(bytes(command, 'utf-8'))
		res = (sock.recv(1073741824)).decode('utf-8')
		if res=='true':
			pass
		else:
			print(res)

def console(nick='guest'):
	# user = "\033[1;31;40m {}".format(nick)
	user = nick
	while True:
		command = input(os.getcwd()+'|'+user+':~$ ')
		cmd = command.split()
		if 'cd' in cmd[0] and len(cmd) > 1:
			try:
				os.chdir(cmd[1])
			except FileNotFoundError:
				try:
					os.chdir(autoincrement(cmd[1]))
				except FileNotFoundError:
					print('No such file in directory')
				except NotADirectoryError:
					print('This is not a directory')
				except TypeError:
					print('No such file in directory')
			except NotADirectoryError:
				print('It\'s not a directory')
		elif cmd[0] == 'cd':
			os.system('cd /')
		elif cmd[0] == 'exit':
			break
		elif cmd[0] == 'pwd':
			print(os.getcwd())
		elif 'cat' in cmd[0]:
			if cmd[1].endswith('.mp3'):
				print('This command cannot read music files')
			elif cmd[1].endswith('.exe'):
				print('This is application, you cannot read this')
			elif cmd[1].endswith('.docx'):
				print('This is word document, you cannot read this')
			else:
				try:
					file = open(cmd[1], 'r')
					print(file.read())
					file.close()
				except UnicodeDecodeError:
					print('You cannot read this file')
				except IsADirectoryError:
					print('This is directory')
				except FileNotFoundError:
					try:
						file = open(autoincrement(cmd[1]))
						print(file.read())
						file.close()
					except UnicodeDecodeError:
						print('You cannot read this file')
					except IsADirectoryError:
						print('This is directory')
					except TypeError:
						print('Error')
		elif cmd[0] == 'xdg-open':
			try:
				os.system(cmd[1])
			except FileNotFoundError:
				try:
					os.system(autoincrement(cmd[1]))
				except FileNotFoundError:
					print('No such file in directory')
				except TypeError:
					print('No such file in directory')
		elif cmd[0] == 'touch':
			file = open(cmd[1], 'w')
			file.close()
		elif cmd[0] == 'mv':
			try:
				shutil.move(cmd[1], cmd[2])
			except FileNotFoundError:
				try:
					shutil.move(autoincrement(cmd[1], autoincrement(cmd[2])))
				except FileNotFoundError:
					print('No such file in directory or directory does not exists')
				except TypeError:
					print('No such file in directory or directory does not exists')
		elif cmd[0] == 'cp':
			try:
				shutil.copy(cmd[1], cmd[2])
			except FileNotFoundError:
				try:
					shutil.copy(autoincrement(cmd[1], autoincrement(cmd[2])))
				except FileNotFoundError:
					print('No such file in directory or directory does not exists')
				except TypeError:
					print('No such file in directory or directory does not exists')
		elif cmd[0] == 'ls':
			if cmd[0] == 'ls' and len(cmd) == 1:
				files = os.listdir()
				for i in files:
					print(i)
			elif cmd[0] == 'ls' and len(cmd) > 1:
				try:
					files = os.listdir(os.getcwd() + '/' + cmd[1])
					for i in files:
						print(i)
				except FileNotFoundError:
					try:
						files = os.listdir(os.getcwd() + '/' + autoincrement(cmd[1]))
						for i in files:
							print(i)
					except TypeError:
						print('Directory does not exists')
				except TypeError:
					try:
						files = os.listdir(os.getcwd() + '/' + autoincrement(cmd[1]))
						for i in files:
							print(i)
					except TypeError:
						print('Directory does not exists')
		elif cmd[0] == 'clear':
			os.system('cls')
		elif cmd[0] == 'rm':
			try:
				os.system('del ' + cmd[1])
			except TypeError:
				try:
					os.system('del ' + autoincrement(cmd[1]))
				except TypeError:
					print('No such file in directory')
		else:
			os.system(command)


try:
	if sys.argv[1] == '-s':
		server(sys.argv[2], sys.argv[3])
	elif sys.argv[1] == '-l':
		try:
			console(sys.argv[2])
		except IndexError:
			console()
except IndexError:
	console()