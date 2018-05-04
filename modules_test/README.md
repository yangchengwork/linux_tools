因建华在询问如何可以开发Linux驱动，我在参考https://blog.csdn.net/tangchao198507/article/details/6122489和https://github.com/jesstess/ldd4/tree/master/simple

执行
make
sudo insmod mymodules.ko
dmesg | tail
sudo rmmod mymodules
dmesg | tail
