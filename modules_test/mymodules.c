#include <linux/module.h>
#include <linux/init.h>
#include <linux/moduleparam.h>

MODULE_AUTHOR("Gump Yang");
MODULE_LICENSE("GPLv3");

static int count = 3;
module_param(count, int, S_IRUGO);

static int __init gump_init(void)
{
    int size, i;
    if (count < 1) {
        size = 3;
    } else {
        size = count;
    }

    for (i=0; i<size; i++) {
        printk(KERN_ALERT "Hello, How are you, %d\n", i);
    }

    return 0;
}

static void __exit gump_exit(void)
{
    printk(KERN_ALERT "I have been unload\n");
}

module_init(gump_init);
module_exit(gump_exit);
