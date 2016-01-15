#-*- coding:utf-8 -*-
#Filename:Sync.py


#用来备份Summary的 
#Filename:backup_ver1.py 
import os 
import time 
import sys 


#备份的源文件路径 
#sourc = '/vault/Mamba-Comm-GND(LAM)-GIS-CD-L00056/Mamba-Comm-GND(LAM)_GIS-CD-L00056_v3.0.5_N66_MP_Summary.csv'
#备份的文件所放的地方 
target_dir = '/vault/Mamba-Comm-GND(LAM)-GIS-CD-L00056/Backup/'
if not os.path.exists(target_dir):
	os.mkdir(target_dir)
def backupCSV(sourc, target_dir):
	#备份文件的名字 
	target = target_dir + time.strftime('%Y%m%d%H%M%S')+'_Summary.zip'
	zip_command = "zip -qr '%s' %s" % (target,''.join("'" + sourc + "'")) 
	#zip_command = "winrar a /"%s/" %s" % (target,' '.join(sourc)) 
	#zip_command="winrar a %s %s" %(target,' '.join(sourc)) 
	#print zip_command 
	if os.system(zip_command) == 0: 
	  print 'Bachup success！'
	else: 
	  print 'Backup failed!'

def getFileList(dir, fileList):
	newDir = dir

	for s in os.listdir(dir):
		if s.startswith('Mamba-Comm-'):
			fileList.append(s)
	return fileList