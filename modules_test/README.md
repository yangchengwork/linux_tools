因建华在询问如何可以开发Linux驱动，我在[参考1](https://blog.csdn.net/tangchao198507/article/details/6122489)和[参考2](https://github.com/jesstess/ldd4/tree/master/simple)后，做了一个最简单的模型

执行
```
make
sudo insmod mymodules.ko
dmesg | tail
sudo rmmod mymodules
dmesg | tail
```