#!/usr/bin/python3

import multiprocessing
import os
import sqlite3
import webbrowser
import random
import ssl
import smtplib
import time
import shutil
import base64
import sys
import socket
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

files_in_dir = os.listdir()
if 'database.db' not in files_in_dir:
	conn = sqlite3.connect('database.db')
	c = conn.cursor()
	c.execute("""CREATE TABLE users(
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			nick text,
			password text,
			gmail text
	)""")
	conn.commit()
	conn.close()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IP = s.getsockname()[0]
s.close()

#======================================MAIN=============================================

#==============================COMMANDS TUTORIAL============================================

def shell_install():
	url = 'https://www.windowscentral.com/install-windows-subsystem-linux-windows-10'
	webbrowser.open(url, new=0, autoraise=True)

def cmd_function(rt, var, exmpl, txt1='', txt2='', txt3='', txt4='', txt5='', txt6='', txt7='', txt8=''):
	global cmd_stat
	rt.configure(bg='white')
	rt.title(str(var))
	cmd_stat = Label(rt, text=var, font=('', 11), bd=5, height='1', width='110').grid(row=0, column=0, sticky=NE)

	info1 = Label(rt, text=txt1, bg='white', font=('', 14))
	info2 = Label(rt, text=txt2, bg='white', font=('', 14))
	info3 = Label(rt, text=txt3, bg='white', font=('', 14))
	info4 = Label(rt, text=txt4, bg='white', font=('', 14))
	info5 = Label(rt, text=txt5, bg='white', font=('', 14))
	info6 = Label(rt, text=txt6, bg='white', font=('', 14))
	info7 = Label(rt, text=txt7, bg='white', font=('', 14))
	info8 = Label(rt, text=txt8, bg='white', font=('', 14))

	info1.grid(row=1, column=0, pady=2)
	info2.grid(row=2, column=0, pady=2)
	info3.grid(row=3, column=0, pady=2)
	info4.grid(row=4, column=0, pady=2)
	info5.grid(row=5, column=0, pady=2)
	info6.grid(row=6, column=0, pady=2)
	info7.grid(row=7, column=0, pady=2)
	info8.grid(row=8, column=0, pady=2)

	exmpl1 = Label(rt, text='Example:', bg='white', font=('', 16)).grid(row=9, column=0, pady=20)
	exmpl2 = Label(rt, text=exmpl, bg='white', font=('', 16)).grid(row=10, column=0, pady=20)

	cmd_ext_bt = Button(rt, text='Close', fg='blue', bg='white', command=rt.destroy)
	cmd_ext_bt.grid(row=100, column=0, pady=10)

def cd_cmd():
	rcd = Toplevel()
	txt1 = 'Kоманда командной строки для изменения текущего рабочего '
	txt2 = ' команда командной строки для изменения текущего рабочего'
	txt3 = 'использования в скриптах командного интерпретатора или в пакетных файлах.'
	exmpl = 'cd <PATH TO THE DIRECTORY ON YOUR COMPUTER>'
	cmd_function(rcd, 'cd', exmpl, txt1, txt2, txt3)
	
def ls_cmd():
	rls = Toplevel()
	txt1 = 'Команда ls – просмотр каталога Команда ls'
	txt2 = 'используется в командной оболочке Linux для'
	txt3 = 'вывода содержимого каталогов и информации о'
	txt4 = 'файлах. ... В качестве аргументов ls принимает'
	txt5 = 'адреса каталогов или файлов.'
	exmpl = 'ls <PATH TO THE DIRECTORY ON YOUR COMPUTER>'
	cmd_function(rls, 'ls', exmpl, txt1, txt2, txt3, txt4, txt5)

def pwd_cmd():
	rpwd = Toplevel()
	txt1 = 'pwd (англ. present working directory — текущий рабочий каталог; или print'
	txt2 = 'working directory — вывести рабочий каталог) — консольная утилита в UNIX-'
	txt3 = 'подобных системах, которая выводит полный путь от корневого каталога к'
	txt4 = 'текущему рабочему каталогу: в контексте которого (по умолчанию) будут'
	txt5 = 'исполняться вводимые команды.'
	exmpl = 'pwd; output: <YOUR PATH>'
	cmd_function(rpwd, 'pwd', exmpl, txt1, txt2, txt3, txt4, txt5)

def touch_cmd():
	rtouch = Toplevel()
	txt1 = 'touch — команда Unix, предназначенная для установки времени'
	txt2 = 'последнего изменения файла или доступа в текущее время. Также используется'
	txt3 = 'для создания пустых файлов.'
	exmpl = 'touch <any file you wanna create>'
	cmd_function(rtouch, 'touch', exmpl, txt1, txt2, txt3)

def mkdir_cmd():
	rmkdir = Toplevel()
	txt1 = 'mkdir (от англ. make directory) в операционной'
	txt2 = 'системе Unix, Linux, DOS, Windows — команда для'
	txt3 = 'создания новых каталогов.'
	exmpl = 'mkdir <NAME OF THE NEW DIRECTORY>'
	cmd_function(rmkdir, 'mkdir', exmpl, txt1, txt2, txt3)

def rm_cmd():
	rrm = Toplevel()
	txt1 = 'remove) — утилита в UNIX и UNIX-подобных системах, используемая для'
	txt2 = 'удаления файлов из файловой системы. Если удаляемый файл не является'
	txt3 = 'каталогом, то ключ -r не влияет на команду rm. -i — выводить запрос на'
	txt4 = 'подтверждение каждой операции удаления.'
	exmpl = 'rm <NAME OF THE FILE YOU WANNA DELETE>'
	cmd_function(rrm, 'rm', exmpl, txt1, txt2, txt3, txt4)

def xdg_opn_cmd():
	ropn = Toplevel()
	txt1 = 'Эта команда открывает файлы в стандартном приложении'
	exmpl = 'xdg-open <NAME OF THE FILE YOU WANNA OPEN IN THE DEFAULT APP'
	cmd_function(ropn, 'xdg-open', exmpl, txt1)

def cp_cmd():
	rcp = Toplevel()
	txt1 = 'cp — команда Unix в составе GNU Coreutils, предназначенная для копирования'
	txt2 = 'файлов из одного в другие каталоги (возможно, с другой файловой системой).'
	txt3 = 'Исходный файл остаётся неизменным, имя созданного файла может быть таким'
	txt4 = 'же, как у исходного, или измениться. В DOS и Windows аналогом является'
	txt5 = 'команда COPY.'
	exmpl = 'cp <FILE OR DIRECTORY> <PATH TO THE DIRECTORY, WHERE YOU WANNA PASTE IT>'
	cmd_function(rcp, 'cp', exmpl, txt1, txt2, txt3, txt4, txt5)

def mv_cmd():
	rmv = Toplevel()
	txt1 = 'mv (от англ. move) — утилита в UNIX и UNIX-подобных системах, используется'
	txt2 = 'для перемещения или переименования файлов. Использование: Если в'
	txt3 = 'качестве аргументов заданы имена двух файлов, то имя первого файла будет'
	txt4 = 'изменено на имя второго.'
	exmpl = 'mv <FILE OR DIRECTORY> <PATH TO THE DIRECTORY, WHERE YOU WANNA MOVE IT>'
	cmd_function(rmv, 'mv', exmpl, txt1, txt2, txt3, txt4)

def cat_cmd():
	rcat = Toplevel()
	txt1 = 'Просмотр, перенаправление и сложение файлов с помощью cat. Эта утилита'
	txt2 = 'называется cat, что является сокращением от "concatenate" (конкатенация), и'
	txt3 = 'используется для склеивания файлов. Команда cat также может вывести'
	txt4 = 'содержимое всего файла на экран (например, введите cat filename. txt).'
	exmpl = 'cat <FILE THAT YOU WANNA READ OR CREATE A NEW ONE>'
	cmd_function(rcat, 'cat', exmpl, txt1, txt2, txt3, txt4)

def clear_cmd():
	rcat = Toplevel()
	txt1 = 'Just type "clear" to clear your screen'
	exmpl = 'clear'
	cmd_function(rcat, 'clear', exmpl, txt1)

def commands():
	global commands
	cmd = Toplevel()
	cmd.configure(bg='white')
	cmd.title('COMMANDS')

	cd = Button(cmd, text='cd', command=cd_cmd, bg='white', font=('', 14), width='10')
	ls = Button(cmd, text='ls', command=ls_cmd, bg='white', font=('', 14), width='10')
	pwd = Button(cmd, text='pwd', command=pwd_cmd, bg='white', font=('', 14), width='10')
	touch = Button(cmd, text='touch', command=touch_cmd, bg='white', font=('', 14), width='10')
	mkdir = Button(cmd, text='mkdir', command=mkdir_cmd, bg='white', font=('', 14), width='10')
	rm = Button(cmd, text='rm', command=rm_cmd, bg='white', font=('', 14), width='10')
	xdg_opn = Button(cmd, text='xdg-open', command=xdg_opn_cmd, bg='white', font=('', 14), width='10')
	mv = Button(cmd, text='mv', command=mv_cmd, bg='white', font=('', 14), width='10')
	cp = Button(cmd, text='cp', command=cp_cmd, bg='white', font=('', 14), width='10')
	cat = Button(cmd, text='cat', command=cat_cmd, bg='white', font=('', 14), width='10')

	cd.grid(row=1, column=0, padx=30, pady=10)
	ls.grid(row=1, column=1, padx=30, pady=10)
	pwd.grid(row=2, column=0, padx=30, pady=10)
	touch.grid(row=2, column=1, padx=30, pady=10)
	mkdir.grid(row=3, column=0, padx=30, pady=10)
	rm.grid(row=3, column=1, padx=30, pady=10)
	xdg_opn.grid(row=4, column=0, padx=30, pady=10)
	mv.grid(row=4, column=1, padx=30, pady=10)
	cp.grid(row=5, column=0, padx=30, pady=10)
	cat.grid(row=5, column=1, padx=30, pady=10)

#======================================================================================================

def console(nick):
	# os.system('console.exe -l ' + nick)
	os.system('console.exe -l ' + nick)

def fdb_recv(email, text):
	global feedback_bt
	global feedb_lbl
	ftext = 'Email: {}\nIP: {}\nFeedback: {}'.format(email, IP, text)
	smtp_server = 'smtp.gmail.com'
	port = 465
	receiver = 'reversflash47@gmail.com'
	sender = 'OSINT48@gmail.com'
	password = 'perehod2020-2021'
	subject = 'Feedback'
	message = """\
	From: {}
	To: {}
	Subject: {}
	
		{}
	""".format(sender, receiver, subject, ftext)
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL(smtp_server, port, context = context) as server:
		server.login(sender, password)
		server.sendmail(sender, receiver, message)
	fdb.destroy()
	feedback_bt.grid_forget()
	feedb_lbl = Label(frm, text='Спасибо', fg='blue', bg='white')
	feedb_lbl.grid(row=0, column=1, sticky=E, padx=5, pady=5, ipadx=5)

def feedback(email):
	global fdb 
	global feedback_bt
	global feedb_lbl
	global frm
	global fdb_inp
	fdb = Toplevel()
	fdb.configure(bg='white')
	fdb.title('Feedback')

	stat = Label(fdb, width='100').grid(row=0, column=0, sticky=NE)

	lbl1 = Label(fdb, text='Вы можете написать здесь что либо.', bg='white')
	lbl2 = Label(fdb, text='После нажатия кнопки', bg='white')
	lbl3 = Label(fdb, text='ваш отзыв будет отправлен разработчикам.', bg='white')
	lbl1.grid(row=1, column=0, padx=10, pady=5)
	lbl2.grid(row=2, column=0, padx=10, pady=5)
	lbl3.grid(row=3, column=0, padx=10, pady=5)

	fdb_inp = Entry(fdb, width='50', bd=2)
	fdb_inp.grid(row=4, column=0, padx=10, pady=10)
	fdb_bt = Button(fdb, text='Send', command=lambda: fdb_recv(email, fdb_inp.get()), bg='white', font=('', 10), fg='blue')
	fdb_bt.grid(row=5, column=0, pady=10, padx=10)

#======================================TEST========================================================================

def finish(v1, v2, v3, v4, v5, v6, v7, v8, v9, v10):
	global forward_bt
	mark = 0 
	if v1 == 4: mark+=1
	if v2 == 3: mark+=1
	if v3 == 4: mark+=1
	if v4 == 1: mark+=1
	if v5 == 3: mark+=1
	if v6 == 2: mark+=1
	if v7 == 1: mark+=1
	if v8 == 2: mark+=1
	if v9 == 1: mark+=1
	if v10 == 3: mark+=1
	finish_mark = ((int(mark) * 100)/len(question_list))
	mark_lbl = Label(tst, text=str(finish_mark)+'%', font=('', 70),fg='#abaaa7', bg='white')
	mark_lbl.grid(row=1, column=0, pady=50)
	forward_bt.grid_forget()
	forward_bt = Button(tst, text='Exit', width='30', command=tst.destroy, bg='white', fg='blue')
	forward_bt.grid(row=2, column=0)

def forward_def(n):
	global question_list 
	global tst
	global tfrm
	global forward_bt
	try:
		tfrm.grid_forget()
		tfrm = question_list[n]
		tfrm.grid(row=1, column=0)
		forward_bt.grid_forget()
		forward_bt = Button(tst, text='Next', command=lambda: forward_def(n+1), bg='white', fg='blue')
		forward_bt.grid(row=2, column=0, pady=10)
	except IndexError:
		forward_bt = Button(tst, text='Finish the test', command=lambda: finish(tst_var1.get(), tst_var2.get(), tst_var3.get(), tst_var4.get(), tst_var5.get(), tst_var6.get(), tst_var7.get(), tst_var8.get(), tst_var9.get(), tst_var10.get()), bg='white', fg='blue')
		forward_bt.grid(row=2, column=0, pady=10)

def start_test_def():
	global tst
	global tst_stat 
	global lbl1, lbl2, lbl3, lbl4, lbl5
	global tst_var1, tst_var2, tst_var3, tst_var4, tst_var5, tst_var6, tst_var7, tst_var8, tst_var9, tst_var10
	global start_bt
	global forward_bt
	global question_list
	global tfrm
	elems = [tst_stat, lbl1, lbl2, lbl3, lbl4, lbl5, start_bt]
	for i in elems:
		i.grid_forget()

	tst_stat = Label(tst, text='TEST', bd=5, height='1', width='90')
	tst_stat.grid(row=0, column=0, sticky=NE)
	tst.geometry('652x300')

	tfrm1 = LabelFrame(tst)
	tfrm1.configure(bg='white')
	question = Label(tfrm1, text='Что делает команда cd? ', bg='white', font=('', 13))
	question.grid(row=0, column=0, padx=50, pady=10)
	tst_var1 = IntVar()
	Radiobutton(tfrm1, text='Создает файлы в папке',variable=tst_var1, value=1, bg='white', font=('', 13)).grid(row=1, column=0, pady=5, padx=10)
	Radiobutton(tfrm1, text='Удаляет все файлы',variable=tst_var1, value=2, bg='white', font=('', 13)).grid(row=2, column=0, pady=5)
	Radiobutton(tfrm1, text='Удаляет файлы',variable=tst_var1, value=3, bg='white', font=('', 13)).grid(row=3, column=0, pady=5)
	Radiobutton(tfrm1, text='Изменяет текущий каталог',variable=tst_var1, value=4, bg='white', font=('', 13)).grid(row=4, column=0, pady=5)

	tfrm2 = LabelFrame(tst)
	tfrm2.configure(bg='white')
	question = Label(tfrm2, text='Что делает команда mv? ', bg='white', font=('', 13))
	question.grid(row=0, column=0, padx=50, pady=10)
	tst_var2 = IntVar()
	Radiobutton(tfrm2, text='Перемещает вас по папкам',variable=tst_var2, value=1, bg='white', font=('', 13)).grid(row=1, column=0, pady=5, padx=10)
	Radiobutton(tfrm2, text='Открывает файлы в Sublime Text 3',variable=tst_var2, value=2, bg='white', font=('', 13)).grid(row=2, column=0, pady=5)
	Radiobutton(tfrm2, text='Перемещает файлы',variable=tst_var2, value=3, bg='white', font=('', 13)).grid(row=3, column=0, pady=5)
	Radiobutton(tfrm2, text='Создает файлы',variable=tst_var2, value=4, bg='white', font=('', 13)).grid(row=4, column=0, pady=5)

	tfrm3 = LabelFrame(tst)
	tfrm3.configure(bg='white')
	question = Label(tfrm3, text='Что делает команда xdg-open? ', bg='white', font=('', 13))
	question.grid(row=0, column=0, padx=50, pady=10)
	tst_var3 = IntVar()
	Radiobutton(tfrm3, text='Создает файлы',variable=tst_var3, value=1, bg='white', font=('', 13)).grid(row=1, column=0, pady=5, padx=10)
	Radiobutton(tfrm3, text='Нет такой команды',variable=tst_var3, value=2, bg='white', font=('', 13)).grid(row=2, column=0, pady=5)
	Radiobutton(tfrm3, text='Показывает путь к папке',variable=tst_var3, value=3, bg='white', font=('', 13)).grid(row=3, column=0, pady=5)
	Radiobutton(tfrm3, text='Открывает файл в приложении',variable=tst_var3, value=4, bg='white', font=('', 13)).grid(row=4, column=0, pady=5)

	tfrm4 = LabelFrame(tst)
	tfrm4.configure(bg='white')
	question = Label(tfrm4, text='Что делает команда rm? ', bg='white', font=('', 13))
	question.grid(row=0, column=0, padx=50, pady=10)
	tst_var4 = IntVar()
	Radiobutton(tfrm4, text='Удаляет файлы',variable=tst_var4, value=1, bg='white', font=('', 13)).grid(row=1, column=0, pady=5, padx=10)
	Radiobutton(tfrm4, text='Пеемещает файлы',variable=tst_var4, value=2, bg='white', font=('', 12)).grid(row=2, column=0, pady=5)
	Radiobutton(tfrm4, text='Создает файлы',variable=tst_var4, value=3, bg='white', font=('', 13)).grid(row=3, column=0, pady=5)
	Radiobutton(tfrm4, text='Нет правильного ответа',variable=tst_var4, value=4, bg='white', font=('', 13)).grid(row=4, column=0, pady=5)

	tfrm5 = LabelFrame(tst)
	tfrm5.configure(bg='white')
	question = Label(tfrm5, text='Что делает команда touch? ', bg='white', font=('', 13))
	question.grid(row=0, column=0, padx=50, pady=10)
	tst_var5 = IntVar()
	Radiobutton(tfrm5, text='Удаляет файлы',variable=tst_var5, value=1, bg='white', font=('', 13)).grid(row=1, column=0, pady=5, padx=10)
	Radiobutton(tfrm5, text='Перемещает файлы',variable=tst_var5, value=2, bg='white', font=('', 13)).grid(row=2, column=0, pady=5)
	Radiobutton(tfrm5, text='Создает файлы',variable=tst_var5, value=3, bg='white', font=('', 13)).grid(row=3, column=0, pady=5)
	Radiobutton(tfrm5, text='Нет правильного ответа',variable=tst_var5, value=4, bg='white', font=('', 13)).grid(row=4, column=0, pady=5)

	tfrm6 = LabelFrame(tst)
	tfrm6.configure(bg='white')
	question = Label(tfrm6, text='Что делает команда ls? ', bg='white', font=('', 13))
	question.grid(row=0, column=0, padx=50, pady=10)
	tst_var6 = IntVar()
	Radiobutton(tfrm6, text='Выключает компьютер',variable=tst_var6, value=1, bg='white', font=('', 13)).grid(row=1, column=0, pady=5, padx=10)
	Radiobutton(tfrm6, text='Показывает файлы в папке',variable=tst_var6, value=2, bg='white', font=('', 13)).grid(row=2, column=0, pady=5)
	Radiobutton(tfrm6, text='Показывает текущие процессы',variable=tst_var6, value=3, bg='white', font=('', 13)).grid(row=3, column=0, pady=5)
	Radiobutton(tfrm6, text='Удаляет файлы',variable=tst_var6, value=4, bg='white', font=('', 13)).grid(row=4, column=0, pady=5)

	tfrm7 = LabelFrame(tst)
	tfrm7.configure(bg='white')
	question = Label(tfrm7, text='Что делает команда cp? ', bg='white', font=('', 13))
	question.grid(row=0, column=0, padx=50, pady=10)
	tst_var7 = IntVar()
	Radiobutton(tfrm7, text='Копрует файлы и папки',variable=tst_var7, value=1, bg='white', font=('', 13)).grid(row=1, column=0, pady=5, padx=10)
	Radiobutton(tfrm7, text='Открывает файл в приложении',variable=tst_var7, value=2, bg='white', font=('', 13)).grid(row=2, column=0, pady=5)
	Radiobutton(tfrm7, text='Взламывает пентагон',variable=tst_var7, value=3, bg='white', font=('', 13)).grid(row=3, column=0, pady=5)
	Radiobutton(tfrm7, text='Перемещает файлы',variable=tst_var7, value=4, bg='white', font=('', 13)).grid(row=4, column=0, pady=5)

	tfrm8 = LabelFrame(tst)
	tfrm8.configure(bg='white')
	question = Label(tfrm8, text='Что делает команда pwd? ', bg='white', font=('', 13))
	question.grid(row=0, column=0, padx=50, pady=10)
	tst_var8 = IntVar()
	Radiobutton(tfrm8, text='Создает файлы',variable=tst_var8, value=1, bg='white', font=('', 13)).grid(row=1, column=0, pady=5, padx=10)
	Radiobutton(tfrm8, text='Показывает текущий путь',variable=tst_var8, value=2, bg='white', font=('', 13)).grid(row=2, column=0, pady=5)
	Radiobutton(tfrm8, text='Удаляет файлы',variable=tst_var8, value=3, bg='white', font=('', 13)).grid(row=3, column=0, pady=5)
	Radiobutton(tfrm8, text='Перемещает вас по папкам',variable=tst_var8, value=4, bg='white', font=('', 13)).grid(row=4, column=0, pady=5)

	tfrm9 = LabelFrame(tst)
	tfrm9.configure(bg='white')
	question = Label(tfrm9, text='Что делает команда mkdir? ', bg='white', font=('', 13))
	question.grid(row=0, column=0, padx=50, pady=10)
	tst_var9 = IntVar()
	Radiobutton(tfrm9, text='Создает папку',variable=tst_var9, value=1, bg='white', font=('', 13)).grid(row=1, column=0, pady=5, padx=10)
	Radiobutton(tfrm9, text='Открывает файл в приложении',variable=tst_var9, value=2, bg='white', font=('', 13)).grid(row=2, column=0, pady=5)
	Radiobutton(tfrm9, text='Создает файлы',variable=tst_var9, value=3, bg='white', font=('', 13)).grid(row=3, column=0, pady=5)
	Radiobutton(tfrm9, text='Пеемещает файлы',variable=tst_var9, value=4, bg='white', font=('', 13)).grid(row=4, column=0, pady=5)

	tfrm10 = LabelFrame(tst)
	tfrm10.configure(bg='white')
	question = Label(tfrm10, text='Что делает команда cat? ', bg='white', font=('', 13))
	question.grid(row=0, column=0, padx=50, pady=10)
	tst_var10 = IntVar()
	Radiobutton(tfrm10, text='Создает папку',variable=tst_var10, value=1, bg='white', font=('', 13)).grid(row=1, column=0, pady=5, padx=10)
	Radiobutton(tfrm10, text='Открывает фаил',variable=tst_var10, value=2, bg='white', font=('', 13)).grid(row=2, column=0, pady=5)
	Radiobutton(tfrm10, text='Показывает содержимое файла',variable=tst_var10, value=3, bg='white', font=('', 13)).grid(row=3, column=0, pady=5)
	Radiobutton(tfrm10, text='Созывает всех котов в городе',variable=tst_var10, value=4, bg='white', font=('', 13)).grid(row=4, column=0, pady=5)

	question_list = [tfrm1, tfrm2, tfrm3, tfrm4, tfrm5, tfrm6, tfrm7, tfrm8, tfrm9, tfrm10]

	tfrm = tfrm1
	tfrm.grid(row=1, column=0)
	forward_bt = Button(tst, text='Next', command=lambda: forward_def(1), bg='white', fg='blue')
	forward_bt.grid(row=2, column=0, padx=10, pady=10)

def test_def():
	global tst
	global tst_stat 
	global lbl1, lbl2, lbl3, lbl4, lbl5
	global start_bt

	tst = Toplevel()
	tst.title('Linux test')
	tst.configure(bg='white')
	tst_stat = Label(tst, text='INFO', bd=5, height='1', width='100')
	tst_stat.grid(row=0, column=0, sticky=NE)

	lbl1 = Label(tst, text='Дайте правильные ответы на все вопросы', bg='white', font=('', 13))
	lbl2 = Label(tst, text='По окончанию теста вы увидите процент', bg='white', font=('', 13))
	lbl3 = Label(tst, text='правильных ответов.', bg='white', font=('', 13))
	lbl4 = Label(tst, text='10 вопросов', bg='white', font=('', 13))
	lbl5 = Label(tst, text='Удачи!', bg='white', font=('', 13))

	lbl1.grid(row=1, column=0, padx=15, pady=2)
	lbl2.grid(row=2, column=0, padx=15, pady=2)
	lbl3.grid(row=3, column=0, padx=15, pady=2)
	lbl4.grid(row=4, column=0, padx=15, pady=2)
	lbl5.grid(row=5, column=0, padx=15, pady=2)

	start_bt = Button(tst, text='Начать тест', bg='white', command=start_test_def, font=('', 14))
	start_bt.grid(row=6, column=0, pady=7)

#=================================================SERVER=========================================================

def connection_to_server(ip, nick):
	# os.system('consle.exe -s ' + ip)
	os.system('console.exe -s ' + ip + ' ' + nick)

def connect_to_server(nick):
	srv = Toplevel()
	srv.title('подключение к серверу')
	srv.configure(bg='white')
	srv_stat = Label(srv, text='подключение', width='100').grid(row=0, column=0, sticky=NE)

	srv_lbl1 = Label(srv, text='1.Запустите server.py на линукс.', bg='white', font=('', 13))
	srv_lbl2 = Label(srv, text='2. Введите IP адрес сервера', bg='white', font=('', 13))
	srv_lbl3 = Label(srv, text='и нажмите "Присоединиться"', bg='white', font=('', 13))
	srv_lbl1.grid(row=1, column=0, padx=10, pady=5)
	srv_lbl2.grid(row=2, column=0, padx=10, pady=5)
	srv_lbl3.grid(row=3, column=0, padx=10, pady=5)

	srv_inp = Entry(srv, width='30', bd=2)
	srv_inp.grid(row=4, column=0, padx=10, pady=10)
	srv_bt = Button(srv, text='Присоединиться', command=lambda: connection_to_server(srv_inp.get(), nick), bg='white', font=('', 10), fg='blue')
	srv_bt.grid(row=5, column=0, pady=10, padx=10)


#================================================================================================================

def documentation():
	url = 'files/index.html'
	webbrowser.open(url, new=0, autoraise=True)

def main(nick='admin'):
	global root
	global logo
	global logo_lbl
	global content_bt
	global nick_err
	global pswrd_err
	global feedback_bt
	global frm

	with sqlite3.connect('database.db') as conn:
		c = conn.cursor()
		c.execute('SELECT * FROM users WHERE nick=(?)', (nick,))
		result = c.fetchall()
	try:
		email = result[0][3]
	except IndexError:
		messagebox.showerror('Error', 'Try again')
	frm = LabelFrame(root)
	frm.grid(row=0, column=0)
	stat = Label(frm, text=nick+ ' || ' + email, font=('', 11), bd=5, height='1', width='100')
	stat.grid(row=0, column=0, sticky=NE, columnspan=2, pady=5)
	feedback_bt = Button(frm, text='Feedback', fg='blue', bg='white', command=lambda: feedback(email))
	feedback_bt.grid(row=0, column=1, sticky=E, padx=5, pady=5)
	
	logo = ImageTk.PhotoImage(Image.open('linux_logo.png'))
	logo_lbl = Label(root, image=logo, bg='white')
	logo_lbl.grid(row=3, column=0, padx=60, pady=10)

	readme1 = Label(root, text='Эта программа покажет вам самые', bg='white', font=('', 14))
	readme2 = Label(root, text='полезные и популярные команды в консоли bash. Консоль Bash - мощный инструмент,', bg='white', font=('', 14))
	readme3 = Label(root, text='полезный для программистови других пользователей, которые хотят научиться', bg='white', font=('', 14))
	readme4 = Label(root, text='выполнять осовные операции за несколько секунд.', bg='white', font=('', 14))
	readme6 = Label(root, text='Вы можете прочитать, как установить проффесиональный эмулятор bash на windows:', bg='white', font=('', 14))
	readme1.grid(row=4, column=0)
	readme2.grid(row=5, column=0)
	readme3.grid(row=6, column=0)
	readme4.grid(row=7, column=0)
	readme6.grid(row=9, column=0)
	url_bt = Button(root, text='Click', fg='blue', bg='white', command=shell_install)
	url_bt.grid(row=10, column=0, pady=5)


	content_bt = Button(root, text='Информация о командах', bg='white', command=commands, font=('', 14))
	content_bt.grid(row=11, column=0, padx=5, pady=10, columnspan=5)
	test_bt = Button(root, text='Пройти тест', bg='white', command=test_def, font=('', 14))
	test_bt.grid(row=12, column=0, padx=5, pady=10, columnspan=5)
	console_bt = Button(root, text='Консоль', bg='white', font=('', 14), command=lambda: console(nick))
	console_bt.grid(row=13, column=0, pady=10)
	server_bt = Button(root, text='Присоединиться к серверу', bg='white', font=('', 14), command=lambda: connect_to_server(nick))
	server_bt.grid(row=14, column=0, pady=10)

#=========================================LOG IN====================================

def rm_login_page():
	global guest_btn
	global nick_lbl
	global nick_inp 
	global password_lbl 
	global password_inp
	global log_btn
	global reg_Btn
	global doc_btn
	elems = [nick_lbl, nick_inp,  password_lbl, password_inp, log_btn, reg_Btn, guest_btn, doc_btn]
	for i in elems:
		i.grid_forget()

def crypt(p):
	p = p.encode()
	salt = b'\x05<\x92\xcb\x10\x06\xc6\x8dh\x99n\xa8\xc3\x83\xca\x94'
	kdf = PBKDF2HMAC(
		algorithm=hashes.SHA256(),
		length = 32,
		salt = salt,
		iterations = 100000,
		backend = default_backend()
	)
	password = base64.urlsafe_b64encode(kdf.derive(p))
	password = password.decode('utf-8')
	return password

def insert_db(nick, email, password, password_conf):
	global rwind
	global chk_bt2
	if password == password_conf:
		password = crypt(password_conf)
		with sqlite3.connect('database.db') as conn:
			c = conn.cursor()
			c.execute('INSERT INTO users(nick, password, gmail) values(?, ?, ?)', (nick, password, email))
			conn.commit()
			rwind.destroy()
	else:
		err_in_pass1 = Label(rwind, text='Пароли не совпадают')
		err_in_pass1.grid()
		try:
			chk_bt2.grid_forget()	
		except NameError:
			pass
		chk_bt2 = Button(rwind, text='Подтвердить', command=lambda:check_code_gmail(nick, email, pass_inp.get(), pass_inp_conf.get()))

def check_code_gmail(var, nick, email):
	global chk_bt
	global chk_code
	global rwind
	global chk_lbl
	if var == code:
		chk_bt.grid_forget()
		chk_code.grid_forget()
		chk_lbl.grid_forget()
		chk_lbl2.grid_forget()
		pass_lbl = Label(rwind, text='Придумайте новый пароль:' ).grid(row=2, column=0, padx=10, pady=10)
		pass_inp = Entry(rwind, width='20', show='*')
		pass_inp.grid(row=2, column=1, padx=10, pady=10)
		pass_lbl_conf = Label(rwind, text='Подтвердите ваш пароль:').grid(row=3, column=0, padx=10, pady=10)
		pass_inp_conf = Entry(rwind, width='20', show='*')
		pass_inp_conf.grid(row=3, column=1, padx=10, pady=10)
		chk_bt2 = Button(rwind, text='Confirm', command=lambda:insert_db(nick, email, pass_inp.get(), pass_inp_conf.get()))
		chk_bt2.grid(row=4, column=0, padx=10, pady=10)
	else:
		err3 = Label(rwind, text='Неверный код').grid(row=4, column=1, pady=10, padx=10)

def gmail_check(receiver='marshallmethers7@gmail.com'):
	global code
	smtp_server = 'smtp.gmail.com'
	port = 465
	sender = 'OSINT48@gmail.com'
	password = 'perehod2020-2021'
	code = str(random.randint(1000, 9999))
	subject = 'OSINT account'
	message = """\
	From: {}
	To: {}
	Subject: {}

	Your code to sign up: {}
	""".format(sender, receiver, subject, code)
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL(smtp_server, port, context = context) as server:
		server.login(sender, password)
		try:
			server.sendmail(sender, receiver, message)
		except smtplib.SMTPRecipientsRefused:
			return 'No account'
		else:
			return 'ok'

def nick_check(nick):
	with sqlite3.connect('database.db') as conn:
		c = conn.cursor()
		c.execute('SELECT * FROM users WHERE nick=(?)', (nick,))
		db_result = c.fetchall()
	if db_result != []:
		return False
	else:
		return True

def check_reg(nick, email):
	global rwind
	global rbt1
	global chk_bt
	global chk_code
	global chk_lbl
	global chk_lbl2
	global rnick_inp
	nickres = nick_check(nick)		
	if nickres == False:
		rnick_inp.delete(0, END)
		rnick_inp.insert(0, 'Пользователь ' + nick + ' уже существует')
	elif nickres == True:
		emres = gmail_check(email)			
		if emres == 'No account':
			remail_inp.delete(0, END)
			remail_inp.insert(0, 'Аккаунт не найден')
		else:
			rbt1.grid_forget()
			chk_lbl = Label(rwind, text='Enter the code that we send to ')
			chk_lbl.grid(row=2, column=0, padx=10)
			chk_lbl2 = Label(rwind, text=email)
			chk_lbl2.grid(row=3, column=0, padx=10)
			chk_code = Entry(rwind, width='10')
			chk_code.grid(row=2, column=1, padx=10, pady=10)
			chk_bt = Button(rwind, text='Confirm', command=lambda: check_code_gmail(chk_code.get(), nick, email))
			chk_bt.grid(row=4, column=0, pady=10, padx=10)	
	else:
		print('i don\'t fucking know what the hell is this, sorry')

def sign_up():
	global rwind
	global rnick_inp
	global remail_inp
	global rbt1
	global rnick_inp
	rwind = Toplevel(root)
	rnick_lbl = Label(rwind, text='Придумайте ник:').grid(row=0, column=0, pady=10, padx=10)
	rnick_inp = Entry(rwind, width='20')
	rnick_inp.grid(row=0, column=1, pady=10, padx=10)
	remail_lbl = Label(rwind, text='Введите ваш google аккаунт:').grid(row=1, column=0, pady=10, padx=10)
	remail_inp = Entry(rwind, width='20')
	remail_inp.grid(row=1, column=1, pady=10, padx=10)

	rbt1 = Button(rwind, text='Submit', command=lambda: check_reg(rnick_inp.get(), remail_inp.get()))
	rbt1.grid(row=2, column=0, pady=10, padx=10)


def sign_in(nick, password):
	global root
	global nick_lbl
	global nick_inp
	global password_inp
	global password_lbl
	with sqlite3.connect('database.db') as conn:
		c = conn.cursor()
		c.execute('SELECT * FROM users WHERE nick=(?)', (nick,))
		db_result = c.fetchall()
	if db_result == []:
		nick_inp.delete(0, END)
		nick_inp.insert(0, 'Пользователь не найден')
	pswrd = crypt(password)
	try:
		if pswrd == db_result[0][2]:
			rm_login_page()
			main(nick)
		else:
			password_inp.delete(0, END)
			nick_inp.delete(0, END)
			nick_inp.insert(0, 'Неверный пароль')
	except IndexError:
		pass

root = Tk()
root.title('LINUX/BASH GUIDE')
root.configure(bg='white')

nick_lbl = Label(root, text='Имя пользователя:', bg='white', font=("", 12))
nick_lbl.grid(row=0, column=0, padx=15, pady=5, columnspan=1)
nick_inp = Entry(root, width="20", bg='white')
nick_inp.grid(row=0, column=1, padx=20)
password_lbl = Label(root, text='Введите пароль:', font=("", 12), bg='white')
password_lbl.grid(row=1, column=0, padx=15, pady=5, columnspan=1)
password_inp = Entry(root, width="20", bg='white', show='*')
password_inp.grid(row=1, column=1, padx=20)

log_btn = Button(root, text='Войти', command=lambda: sign_in(nick_inp.get(), password_inp.get()), width='13', font=('', 10), bg='white')
log_btn.grid(row=2, column=0, pady=15, padx=20, ipadx=5, columnspan=1)
reg_Btn = Button(root, text='Зарегестрироваться', command=sign_up, width='15', height='1', font=('', 10), bg='white')
reg_Btn.grid(row=2, column=1, padx=15, pady=15, ipadx=5)

guest_btn = Button(root, text='Запустить консоль', command=lambda: console('guest'), bg='white', font=('', 10), fg='blue', width='20', height='1')
guest_btn.grid(row=3, column=0, padx=50, pady=5, sticky=NE)
doc_btn = Button(root, text='Документация', command=documentation, bg='white', font=('', 10), fg='blue', width='20', height='1')
doc_btn.grid(row=3, column=1)

root.mainloop()