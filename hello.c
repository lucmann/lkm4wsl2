#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h>

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Luc Ma");
MODULE_DESCRIPTION("A Hello World Kernel Module for WSL2.");
MODULE_VERSION("0.1.0");

static char *name = "world";
module_param(name, charp, S_IRUGO);
MODULE_PARM_DESC(name, "The name to display in /var/log/kern.log");

static int __init hello_wsl2_init(void)
{
	printk(KERN_INFO "WSL2: Hello %s from the WSL2 LKM!\n", name);
	return 0;
}

static void __exit hello_wsl2_exit(void)
{
	printk(KERN_INFO "WSL2: Goodbye %s from the WSL2 LKM!\n", name);
}

module_init(hello_wsl2_init);
module_exit(hello_wsl2_exit);

