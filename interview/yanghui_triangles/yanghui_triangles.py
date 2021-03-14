# -*- coding: utf-8 -*-
#!/usr/bin/env python

def yanghui(num):
    L = [1]
    print(L)
    for j in range(num):
        # yield L
        L = [sum(i) for i in zip([0]+L, L+[0])]
        print(L)

def main_func():
    yanghui(10)

if __name__ == '__main__':
    main_func()