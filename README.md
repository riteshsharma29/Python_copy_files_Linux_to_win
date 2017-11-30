# Python_copy_files_Linux_to_win
Python based script to copy files from linux server / machine to windows machine

Installation & Requirements :

python paramiko library [Install using pip.exe]
Putty
Putty based pscp.exe needs to copied into C:\Windows\System32 folder.

Parameters to be updated in the script :

IPaddress = "192.168.*.*" #Update IP
user = "****" #Update username
passwd = '*******' #Update password

#mycmd varaible needs to be updated with ; seprated linux commands to navigate to the file path and list them.
mycmd = 'cd /root/Downloads/test;ls'
#Linux files source path
source_path = '/root/Downloads/test/'
#windows output directory \\ seprated
outdir = ' e:\\dest\\'

References:

#https://stackoverflow.com/questions/32725229/run-linux-commands-from-windows-in-python-script
#http://www.binbert.com/blog/2011/04/secure-file-transfer-from-windows-to-linux-using-rsa-key/
