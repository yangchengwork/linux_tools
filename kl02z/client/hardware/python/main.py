#!/usr/bin/env python
# -*- coding: utf-8 -*

import serial;
import time, re;

# import threading;
import _thread
import requests;
from urllib3 import encode_multipart_formdata;

COMPATH = "/dev/ttyACM0"
COMBPS = 115200


class MSerialPort:
    message = ""
    counter = 0
    x = []
    y = []
    z = []

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
        self.x = [];
        self.y = [];
        self.z = [];
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
            self.x.append(int(m[0]));
            self.y.append(int(m[1]));
            self.z.append(int(m[2]));
            # print(dataStr, x, y, z);

    def getEndData(self):
        # self.x /= self.counter;
        # self.y /= self.counter;
        # self.z /= self.counter;
        return {'x':self.x, 'y':self.y, 'z':self.z};
        
def post_test(data):
    # requests.get('http://localhost:5000/kl02z')             # GET请求
    # requests.post("http://localhost:5000/kl02z")            # POST请求
    headers = {'content-type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'};

    # data = {'name': 'letian', 'password': '123'};

    # print(type(data), data);
    # data = str(data);
    # print(type(data), data);
    buf = {}
    for i in data:
        bufStr = ",".join('%s' %id for id in data[i]);
        # print(i, bufStr);
        buf[i] = bufStr;
    print(buf);

    """
    encode_data = encode_multipart_formdata(data)
    data = encode_data[0]
    headers['Content-Type'] = encode_data[1]
    """
    # r = requests.post("http://localhost:5000/kl02z", data=data, headers=headers);
    r = requests.post("http://localhost:5000/kl02z", data=buf);
    print(r.text);

def main():
    mSerial = MSerialPort(COMPATH, COMBPS)
    _thread.start_new_thread(mSerial.read_data, ())
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
    data = mSerial.getEndData();
    # print(data);
    post_test(data);
    mSerial.port_close()


if __name__ == "__main__":
    main()

