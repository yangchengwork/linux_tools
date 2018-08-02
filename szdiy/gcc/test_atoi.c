/*
 * 因为SZDIY有人提到在使用atoi时，在GCC
 * 的编译器中会有问题，所以测试一下
 */

#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	unsigned char buf[4];
	unsigned char buf1[2] = {0x30, 0x31};
	unsigned int  number = 0;

	buf[0] = '1';
	buf[1] = '2';
	buf[2] = '8';
	buf[3] = '0';
	number = atoi(buf);
	printf("test out number=%d\r\n", number);
	return 0;
}
