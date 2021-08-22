# A Hello World Linux kernel module for WSL2

## Purposes
0. Build a Hello World LKM based on [WSL2 kernel](https://github.com/microsoft/WSL2-Linux-Kernel)
1. Cross-create a [DKMS](https://github.com/dell/dkms) debian source package for the module

## Preparation
### Build a Hello World LKM base on WSL2 kernel
00. Download linux-msft-wsl-x.y.z.w.tar.gz and untar to `/usr/src/kernels`
01. Configure the downloaded linux source tree

    It is essential to configure the linux source tree and make some targets before building your own LKM.
    ```bash
    cd /usr/src/kernels/WSL2-Linux-Kernel-linux-msft-wsl-x.y.z.w
    zcat /proc/config.gz > .config
    make -j ${nproc}
    make -j ${nproc} modules_install # will install /lib/modules/$(uname -r)
    ```
### Cross-create a DKMS debian source package
00. What is DKMS?

    Dynamic Kernel Module Support(DKMS) is a program/framework that enables generating Linux kernel modules
    whose sources generally reside the kernel source tree. The concept is to have DKMS modules automatically
    rebuilt when a new kernel is installed.(Wikipedia)

01. Why cross-create?

    To create a DKMS debian package requires several tools. It turns out to be easy on the Debian-like platforms.
    However sometimes it is also possible to create a debian package on the RedHat-like platforms.

02. Which tools are needed?

    - dpkg
    - debhelper
    - dkms

### Build perf
```
cd /usr/src/kernels/WSL2-Linux-Kernel-linux-msft-wsl-x.y.z.w/tools/perf
make && make install
cp perf /usr/bin
```

