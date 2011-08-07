#!/usr/bin/env python
### Code adapted from http://code.activestate.com/recipes/299207-console-text-progress-indicator-class/
import sys

# setup the colors for the console display
GREEN = "\033[1;32m"
BLUE = "\033[1;36m"
RED = "\033[1;31m"
LILAC = "\033[1;35m"
YELLOW = "\033[1;33m"
OFF = "\033[1;0m"


class progressbar(object):
	def __init__(self, finalcount, block_char='.', bar_title='FILE'):
		self.finalcount = finalcount
		self.blockcount = 0
		self.block = block_char
		self.f = sys.stdout
		if not self.finalcount: return
		self.f.write(BLUE)
		self.f.write('\n==================================================\n')
		self.f.write('  Downloading: %s %s %s' % (RED,bar_title,BLUE))
		self.f.write('\n==================================================\n')		
		self.f.write('\n------------------- % Progress ------------------1\n')
		self.f.write('    1    2    3    4    5    6    7    8    9    0\n')
		self.f.write('----0----0----0----0----0----0----0----0----0----0\n')
		self.f.write('\n')
		self.f.write(OFF)
	def progress(self, count):
		count = min(count, self.finalcount)
		if self.finalcount:
			percentcomplete = int(round(100.0*count/self.finalcount))
			if percentcomplete < 1: percentcomplete = 1
		else:
			percentcomplete=100
		blockcount = int(percentcomplete//2)
		if blockcount <= self.blockcount:
			return
		for i in range(self.blockcount, blockcount):
			self.f.write(RED)
			self.f.write(self.block)
		self.f.write(OFF)
		self.f.flush()
		self.blockcount = blockcount
		if percentcomplete == 100:
			self.f.write("\n")


if __name__ == "__main__":
	from time import sleep
	pb = progressbar(8, "*")
	for count in range(1, 9):
		pb.progress(count)
		sleep(1)
	pb = progressbar(100)
	for i in range(0,101):
		pb.progress(i)
		sleep(0.3)
