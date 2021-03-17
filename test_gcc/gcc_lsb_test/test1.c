/*
 * 杨城用于测试日期小端组合
 * 日期为 19/01/17 17:05:35
 * 传输数据为 93 88 B1 18 01
 */

#include "stdio.h"
#include "stdlib.h"

void main(void)
{
	// unsigned char sdata[5] = {0x93, 0x88, 0xB1, 0x18, 0x01};
	// 4B801286006A44485805016944489808
	// unsigned char sdata[5] = {0x6A, 0x44, 0x48, 0x58, 0x05};
	// unsigned char sdata[5] = {0x69, 0x44, 0x48, 0x98, 0x08};
	// unsigned char sdata[5] = {0x69, 0x44, 0x48, 0x98, 0x08};
	unsigned char sdata[5] = {0x99, 0xC4, 0x4E, 0x88, 0x09};
	unsigned long long number = 0;

	number = sdata[4];
	number = (number << 8) + sdata[3];
	number = (number << 8) + sdata[2];
	number = (number << 8) + sdata[1];
	number = (number << 8) + sdata[0];

	int type = 0;
	int year = 2000;
	int month = 0;
	int day = 0;
	int hour = 0;
	int minute = 0;
	int second = 0;

	type = number & 0x7;
	year = year + ((number >> 3) & 0x7f);
	month = (number >> 10) & 0x0f;
	day = (number >> 14) & 0x1f;
	hour = (number >> 19) & 0x1f;
	minute = (number >> 24) & 0x3f;
	second = (number >> 30) & 0x3f;

	printf("type=%d %04d/%02d/%02d %02d:%02d:%02d\r\n", type, year, month, day, hour, minute, second);	
}
