#!/usr/bin/python
# coding: utf-8 -*-

import paramiko
import os
import codecs
import sys

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#Linux credentials
#Update IP
IPaddress = "192.*.*.*"
#Update username
user = "****"
#Update password
passwd = '*****'

ssh.connect(IPaddress, username=user, password=passwd, port=22)

mycmd = 'cd /root/Downloads/test;ls'
source_path='/root/Downloads/test/'
outdir = ' e:\\dest\\'

mybatch = codecs.open('my.bat','w',encoding='utf-8')

myfiles=[]

stdin, stdout, stderr = ssh.exec_command(mycmd)
lines = stdout.readlines()
errors = stderr.readlines()
for e in errors:
     print 'error', e
for l in lines:
    l.strip('\n')
    myfiles.append(l)

for myfile in myfiles:
    myfile = myfile.replace(chr(10),"")
    var = 'pscp.exe -pw ' + passwd + ' ' + user + '@' + IPaddress + ':' + source_path +  myfile + outdir
    os.system('pscp.exe -pw ' + passwd + ' ' + user + '@' + IPaddress + ':' + source_path +  myfile + outdir)
    mybatch.write(var)
