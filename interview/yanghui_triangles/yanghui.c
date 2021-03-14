#include <stdio.h>
#include <string.h>

void yanghui_twobuf(int num)
{
    int a[num+1];
    int b[num+1];
    int i, j;

    // 初始化数组
    memset(a, 0, sizeof(int)*(num+1));
    memset(b, 0, sizeof(int)*(num+1));

    for (i=1; i<=num; i++) {
        a[0] = 1;
        b[0] = 1;
        for (j=0; j<i; j++) {
            if (a[j] > 0) {
                b[j+1] = a[j] + a[j+1];
            } else {
                break;
            }
        }
        memcpy(&a[0], &b[0], sizeof(int)*(num+1));
    }

    printf("end line=");
    for (i=0; i<=num; i++) {
        printf("%d ", a[i]);
    }
    printf("\n");
}

// 这是网上的最优的方法
int main_func()
{
    int s = 1, h;                    // 数值和高度
    int i, j;                        // 循环计数
    scanf("%d", &h);                 // 输入层数
    printf("1\n");                   // 输出第一个 1
    for (i = 2; i <= h; s = 1, i++)         // 行数 i 从 2 到层高
    {
        printf("1 ");                // 第一个 1
        for (j = 1; j <= i - 2; j++) { // 列位置 j 绕过第一个直接开始循环
            printf("%d ", (s = (i - j) * s / j));
        }
        printf("1\n");               // 最后一个 1，换行
    }
    getchar();                       // 暂停等待
    return 0;
}



void main(void)
{
    // yanghui(10);
    main_func();
}
