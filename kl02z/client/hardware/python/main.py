#!/usr/bin/env python
# -*- coding: utf-8 -*

import serial;
import time;
# import threading;
import _thread; 

COMPATH = "/dev/ttyACM0";
COMBPS = 115200;

class MSerialPort:
	message=''
	def __init__(self,port,buand):
		self.port=serial.Serial(port,buand)
		if not self.port.isOpen():
			self.port.open()
	def port_open(self):
		if not self.port.isOpen():
			self.port.open()
	def port_close(self):
		self.port.close()
	def send_data(self,data):
		number=self.port.write(data)
		return number
	def read_data(self):
		while True:
			data=self.port.readline()
			self.message=data

def main():
	mSerial=MSerialPort(COMPATH, COMBPS)
	_thread.start_new_thread(mSerial.read_data,())
    # thread_read = threading.Thread(target=mSerial.read_data)
    # thread_read.start();
	while True:
		# time.sleep(1)
		print(mSerial.message)
		print('next line')
    # mSerial.close();

if __name__ == '__main__':
    main();