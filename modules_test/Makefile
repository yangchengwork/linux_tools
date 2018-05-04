# Add your debugging flag (or not) to ccflags.
ifeq ($(DEBUG),y)
  DEBFLAGS = -O -g # "-O" is needed to expand inlines
else
  DEBFLAGS = -O2
endif

ccflags-y += $(DEBFLAGS)

obj-m := mymodules.o
modules-objs := gumpmod.o

KDIR ?= /lib/modules/`uname -r`/build

PWD := $(shell pwd)

default:
	make -C $(KDIR) M=$(PWD) modules

clean:
	rm -rf *.o *.cmd *.ko *.mod.c .tmp_version
