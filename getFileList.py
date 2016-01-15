import os
def getDirList(dir, dirList):
	newDir = dir

	for s in os.listdir(dir):
		if s.startswith('Mamba-Comm-'):
			dirList.append(s)
	return dirList
dirlist = getDirList('/vault/', [])
for x in dirlist:
	print getDirList ('/vault/' + x, [])

def getFileList(dir, fileList):
	newDir = dir

	if os.path.isfile(dir):
		fileList.append()
