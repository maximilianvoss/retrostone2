# Retrostone 2 Pro
This small repository contains a couple helpers, scripts and documentation around the Retrostone 2 Pro.  
It represents also how I set up my Retrostone 2 Pro and will be the foundation for my next installation.     
The Retrostone 2 Pro can be purchased on http://8bcraft.com.

## Setup Retrostone 2
1. Download from http://www.retrorangepi.org/download/
2. Flash SD Card
3. Run Installation
4. Setup wifi
5. Upload SSH keys for simpler login   
    Default password for user `pi` is `pi`.  
    Default password for `root` is `orangepi`.
    ```bash      
    ssh root@rs2 "mkdir ~/.ssh"
    scp ~/.ssh/id_rsa.pub root@rs2:~/.ssh/authorized_keys
    ssh pi@rs2 "mkdir ~/.ssh"
    scp ~/.ssh/id_rsa.pub pi@rs2:~/.ssh/authorized_keys
    ```
6. Change the user passwords  
    Default password for user `pi` is `pi`.  
    Default password for `root` is `orangepi`.
    ```bash
    ssh root@rs2 passwd
    ssh pi@rs2 passwd
    ```
7. Format eMMC storage for the home directory    
    **(This step is only necessary on the very first setup of the Retrostone. If it was done before, please skip)**
    ```bash
    ssh pi@rs2
    sudo fdisk /dev/mmcblk1
    ```
    `p` to list all partitions, then `d` and a number to delete all existing partitions, then `w` to write the changes
    `n` to create a new partition, then use all the defaults, then `w` to write the changes.
    
    Format disk and copy home directory (**you have to ensure that you are not in a directory under /home**)
    ```bash
    sudo mkfs.ext4 -L "emmc" /dev/mmcblk1p1
    sudo mount /dev/mmcblk1p1 /mnt
    sudo mv /home /mnt
    sudo umount /mnt
    ```
    
8. Add disk to the fstab so it is mounted on boot
    ```bash
    sudo cat >>/etc/fstab
    /dev/mmcblk1p1      /home       ext4    defaults    0   0
    ```