/*
 * 杨城用于测试日期小端组合
 * 日期为 19/01/17 17:05:35
 * 传输数据为 93 88 B1 18 01
 */

#include "stdio.h"
#include "stdlib.h"

void main(void)
{
	unsigned char sdata[5] = {0x93, 0x88, 0xB1, 0x18, 0x01};
	unsigned long long number = 0;

	number = 0x01;
	number = (number << 8) + 0x18;
	number = (number << 8) + 0xB1;
	number = (number << 8) + 0x88;
	number = (number << 8) + 0x93;

	int year = 2000;
	int month = 0;
	int day = 0;
	int hour = 0;
	int minute = 0;
	int second = 0;

	year = year + (number & 0x7f);
	month = (number >> 7) & 0x0f;
	day = (number >> 11) & 0x1f;
	hour = (number >> 16) & 0x1f;
	minute = (number >> 21) & 0x3f;
	second = (number >> 27) & 0x3f;

	printf("%04d/%02d/%02d %02d:%02d:%02d\r\n", year, month, day, hour, minute, second);	
}
