#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os,codecs,commands
from itertools import izip, izip_longest
import sys
reload(sys)
sys.setdefaultencoding('utf8')

###################################################################################################################################################

previous_cycle = "/root/Desktop/des_tool/SQ_Master_0516/Movies"
current_cycle = "/root/Desktop/des_tool/SQ_Master_0616/Movies"
output = "/root/Desktop/des_tool/sq_output/Movies"

###################################################################################################################################################


file_1 = codecs.open('log_1.txt','w',encoding="utf-8")
file_2 = codecs.open('log_2.txt','w',encoding="utf-8")

def calc_chksum_1():
	for subdir, dirs, files in os.walk(previous_cycle):
		for file in files:
			#print os.path.join(subdir, file)
			fl1 = os.path.join(subdir, file)
			#if os.path.join(subdir, "Thumbs.db"): os.system("rm -Rf " + os.path.join(subdir, "Thumbs.db"))
			fl1 = fl1.encode('utf-8')
			fl1 = "'" + str(fl1) + "'"
			cksum_1 = commands.getstatusoutput("/usr/bin/cksum " + fl1 + " | awk '{ print $1 }'")
			cksum_1 = cksum_1[1]
			file_1.write(fl1 + "=" + str(cksum_1) + '\n')

def calc_chksum_2():
	for subdir, dirs, files in os.walk(current_cycle):
		for file in files:
			#print os.path.join(subdir, file)
			fl1 = os.path.join(subdir, file)
			#if os.path.join(subdir, "Thumbs.db"): os.system("rm -Rf " + os.path.join(subdir, "Thumbs.db"))
			fl1 = fl1.encode('utf-8')
			fl1 = "'" + str(fl1) + "'"
			cksum_1 = commands.getstatusoutput("/usr/bin/cksum " + fl1 + " | awk '{ print $1 }'")
			cksum_1 = cksum_1[1]
			file_2.write(fl1 + "=" + str(cksum_1) + '\n')


calc_chksum_1()
calc_chksum_2()

###################################################################################################################################################


input_file = open('log_1.txt', 'r')

mylist = []
for line in input_file:
	line1 = line.rstrip('\n')
	x1, y1 = line1.split('=', 1)
	mylist.append(str(y1))
for vals in mylist:
	input_file_2 = open('log_2.txt', 'r')
	for line_2 in input_file_2:
		line2 = line_2.rstrip('\n')
		x2, y2 = line2.split('=', 1)
		if str(y2) == str(vals):
			outpath = x2.replace(current_cycle,output)
			os.system('cp ' + x2 + ' ' + outpath)
			
