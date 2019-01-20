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
	int year = 2000;
	int month = 0;
	int day = 0;
	int hour = 0;
	int minute = 0;
	int second = 0;

	year = year + (sdata[0] & 0x7f);
	month = ((sdata[0] >> 7) & 0x01) + ((sdata[1] << 1) & 0x0E);
	day = (sdata[1] >> 3) & 0x1f;
	hour = (sdata[2] & 0x1f);
	minute = ((sdata[2] >> 5) & 0x07) + ((sdata[3] << 3) & 0x38);
	second = ((sdata[3] >> 3) & 0x1f) + ((sdata[4] & 0x01) << 5);

	printf("%04d/%02d/%02d %02d:%02d:%02d\r\n", year, month, day, hour, minute, second);	
}
