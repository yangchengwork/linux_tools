#!/usr/bin/env python
# -*- coding: utf-8 -*

import serial;
import time, re;

# import threading;
import _thread

COMPATH = "/dev/ttyACM0"
COMBPS = 115200


class MSerialPort:
    message = ""
    counter = 0
    x = 0
    y = 0
    z = 0

    def __init__(self, port, buand):
        self.port = serial.Serial(port, buand)
        if not self.port.isOpen():
            self.port.open()

    def port_open(self):
        if not self.port.isOpen():
            self.port.open()

    def port_close(self):
        self.port.close()

    def send_data(self, data):
        number = self.port.write(data)
        return number

    def read_data(self):
        self.counter = 0
        self.x = self.y = self.z = 0;
        self.port.flushInput();
        while True:
            try:
                data = self.port.readline();
                # print(data, data.decode());
                self.data_judge(data.decode());
                self.counter += 1
                # self.message = data
            except serial.serialutil.SerialException:
                print("read exception");
                break;
            except:
                print("termios error");
                break;

    def data_judge(self, dataStr):
        # pattern = re.compile(r'=');
        pattern = re.compile(r'(-*\d+)');
        m = pattern.findall(dataStr);
        # print(dataStr, m);
        if len(m) == 3:
            self.x += int(m[0]);
            self.y += int(m[1]);
            self.z += int(m[2]);
            # print(dataStr, x, y, z);

    def getEndData(self):
        self.x /= self.counter;
        self.y /= self.counter;
        self.z /= self.counter;
        return (self.x, self.y, self.z);
        

def main():
    mSerial = MSerialPort(COMPATH, COMBPS)
    _thread.start_new_thread(mSerial.read_data, ())
    # thread_read = threading.Thread(target=mSerial.read_data)
    # thread_read.start();
    """
    while True:
        time.sleep(1)
        a = input("input:").lower();
        if a == 'q':
            break;
        print(mSerial.message)
        print('next line')
    """
    time.sleep(1)
    print(mSerial.getEndData());
    mSerial.port_close()


if __name__ == "__main__":
    main()

