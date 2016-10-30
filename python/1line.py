#!/usr/bin/env python

import os
import sys
import time

scale = [(0.07, 0.14), (0.05, 0.1)]

def my_heart():
	for i in range(len(scale)):
		os.system('clear')
		print('\n'.join([''.join([('LoveLn'[(x-y)%6] if ((x*scale[i][0])**2+(y*scale[i][1])**2-1)**3-(x*scale[i][0])**2*(y*scale[i][1])**3 <= 0 else ' ') for x in range(-30,30)]) for y in range(15,-15,-1)]))
		time.sleep(0.2)

if __name__ == '__main__':
	print('\033[1;31m')
	while (True):
		my_heart()
		time.sleep(0.3)
