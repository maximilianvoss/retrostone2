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
    
    
## Auto shutdown when battery goes low
A small shell script which observes the battery state. If < 3% of capacity is left, it will beep 5 times and afterwards call `shutdown -h 3` so you have 3 minutes to save all game state before it is going to be shutdown. 
```bash
sudo cp src/autoshutdown.service /etc/systemd/system/
sudo cp src/autoshutdown.sh /usr/bin/
sudo chmod 755 /usr/bin/autoshutdown.sh
sudo systemctl enable autoshutdown.service
sudo systemctl start autoshutdown.service
```

## WiFi in the Retropie Menu
Adding the Enable WiFi switch dirctly into the Retropie Menu as it is annoying always having to open a submenu to do so.
```bash
ln -s ~/RetroPie/retropiemenu/RetrOrangePi/Wifi/Enable.sh ~/RetroPie/retropiemenu/Enable\ Wifi.sh
```

## Resetting the Gamepad after it got stuck with holding a key
```bash
cp src/Reset\ Gamepad.sh ~/RetroPie/retropiemenu/Reset\ Gamepad.sh
chmod 755 ~/RetroPie/retropiemenu/Reset\ Gamepad.sh
```

