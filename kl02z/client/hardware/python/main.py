#!/usr/bin/env python
# -*- coding: utf-8 -*

import serial;

COMPATH = "/dev/ttyACM0";
COMBPS = 115200;

def main():
    ser = serial.Serial(COMPATH, COMBPS, timeout=0.5);
    for i in range(0, 10):
        print(ser.readline());
    ser.close;

if __name__ == '__main__':
    main();