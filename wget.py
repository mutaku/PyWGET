#!/usr/bin/env python

## Guido's custom wget

import sys,urllib,math,os,time
CURDIR = os.getcwd()
sys.path.append(CURDIR)
import prog

size = 0

def reporthook(*a):
	global size
	#print a
	size = float(a[2])
	steps = float(math.ceil(size/8192))
	s = float(a[0])/steps*100
	pb.progress(s)	

for url in sys.argv[1:]:
	i = url.rfind('/')
	file = url[i+1:]
	if os.path.exists(file):
		fa = os.path.splitext(file)[0]
		fb = os.path.splitext(file)[1]
		fs = '_'+str(int(time.time()))
		file = fa+fs+fb	
	print
	pb = prog.progressbar(100,'*',url)
	urllib.urlretrieve(url, file, reporthook)
	print
	print url, "->", file, "size=", size, " bytes"
	print
