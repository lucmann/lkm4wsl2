#!/usr/bin/env python

import os
import sys
import time
import ctypes
import signal

"""
Windows Stdout Handles
"""
STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE = -11
STD_ERROR_HANDLE = -12

win_stdout_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

scale = [(0.07, 0.14), (0.05, 0.1)]

def set_win32cmd_text_color(color, handle=win_stdout_handle):
	ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)

def my_heart():
	for i in range(len(scale)):
		if ('posix' == os.name):
			os.system('clear')
		else:
			os.system('cls')
		print('\n'.join([''.join([('LoveLn'[(x-y)%6] if ((x*scale[i][0])**2+(y*scale[i][1])**2-1)**3-(x*scale[i][0])**2*(y*scale[i][1])**3 <= 0 else ' ') for x in range(-30,30)]) for y in range(15,-15,-1)]))
		time.sleep(0.2)

def sigint_handler(signum, frame):
	set_win32cmd_text_color(0x07)
	print('Catched Interrupt Signal!')

if __name__ == '__main__':
	signal.signal(signal.SIGINT, sigint_handler)
	signal.signal(signal.SIGTERM, sigint_handler)

	if ('posix' == os.name):
		print('\033[1;31m')
	else:
		set_win32cmd_text_color(0x0c)

	while True:
		my_heart()
		time.sleep(0.3)
