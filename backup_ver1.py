#-*- coding:utf-8 -*-

#用来备份Summary的 
#Filename:backup_ver1.py 
import os 
import time 
import sys 


SECONDS_PER_DAY = 24 * 60 * 60

def doFirst():
    from datetime import datetime, timedelta
    # 现在的时间
    curTime = datetime.now()
    # 目标时间
    desTime = curTime.replace(hour=6, minute=40, second=0, microsecond=0)
    if desTime > curTime:
        skipSeconds = (desTime - curTime).total_seconds()
    else:
        delta = curTime - desTime
        print delta
        skipSeconds = SECONDS_PER_DAY - delta.total_seconds()
    print "Must sleep %d seconds" % skipSeconds
    return skipSeconds

def backupCSV(sourc, target_dir):
	#备份文件的名字 
	target = target_dir + time.strftime('%Y%m%d%H%M%S')+'_Summary.zip'
	zip_command = "zip -qr '%s' %s" % (target,''.join("'" + sourc + "'")) 
	#zip_command = "winrar a /"%s/" %s" % (target,' '.join(sourc)) 
	#zip_command="winrar a %s %s" %(target,' '.join(sourc)) 
	#print zip_command 
	if os.system(zip_command) == 0: 
		os.remove(sourc)
	  	print 'Bachup success！'
	else: 
	  	print 'Backup failed!'

def getFileList(dir, fileList):
	newDir = dir

	for s in os.listdir(dir):
		if s.startswith('Mamba-Comm-'):
			fileList.append(s)
	return fileList

#遍历文件夹并备份
vault = getFileList('/vault/', [])
def startBackup():
	for x in vault:
		#创建文件备份位置和确认
		#target_dir = '/vault/' + x + '/Backup/'
		#将所有csv备份到/backups/下
		target_dir = '/backups/'
		sourc = '/vault/' + x + '/'
		if not os.path.exists(target_dir):
			os.mkdir(target_dir)
		for n in getFileList(sourc, []):
			if (sourc + n).endswith('.csv'):
				backupCSV(sourc + n, target_dir)
	sleepTime()		#启动下一次备份等待
def sleepTime():
	print "Start timing..."
	time.sleep(doFirst())	#等待下一次备份
	startBackup()			#开始备份
	print "end timeng"
sleepTime()