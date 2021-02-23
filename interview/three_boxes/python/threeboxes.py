# -*- coding: UTF-8 -*-

import random

def main_func():
    changeCount = 0
    keepCount = 0
    maxCount = 1000000

    for i in range(maxCount):
        boxes = [0, 0, 0]

        # 放入盒子
        rIndex = random.randint(0, 2)
        boxes[rIndex] = 1

        # 随机选择
        rSelect = random.randint(0, 2)

        # 打开没有的
        rOpen = 0
        for n in range(3):
            if rOpen == rIndex:
                continue
            elif rOpen == rSelect:
                continue
            else:
                rOpen = n
        
        # 这里有点已经知道结果的味道
        if rIndex == rSelect:
            keepCount += 1
        else:
            changeCount += 1
    
    print("改变选择比例={:.2f}% 不改变选择比例={:.2f}%".format(changeCount*100/maxCount, keepCount*100/maxCount))

if __name__ == '__main__':
    main_func()