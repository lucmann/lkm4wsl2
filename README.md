# A Hello World Linux kernel module for WSL2

## Purposes
0. Build a Hello World LKM based on [WSL2 kernel](https://github.com/microsoft/WSL2-Linux-Kernel)
1. Cross-create a [DKMS](https://github.com/dell/dkms) debian source package for the module

## Preparation
0. Build a Hello World LKM base on WSL2 kernel

00. Download linux-msft-wsl-4.19.y.zip as linux-headers-$(uname -r)
01. Configure the downloaded linux source tree
    It is essential to configure the linux source tree and make some targets before building your own LKM.
    ```bash
    cd /usr/src/kernels/WSL2-Linux-Kernel-linux-msft-wsl-4.19.y
    make oldconfig && make prepare
    make scripts    # for /bin/sh: scripts/mod/modpost
    make modules    # for WARNING: symbol version dump ./Module.symvers is missing
    ```
