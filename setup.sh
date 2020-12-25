#created by MrHacker-X; give me credit if you're using any part of this script.
#bin/bash
clear
bash main/banner.sh
echo
echo
cd main;chmod +x *;cd ..;cd core;chmod +x *;cd ..;cd pass;chmod +x *
termux-setup-storage
cd $HOME
pkg install python -y
pkg install python2 -y
pkg install tor -y
pkg install wget -y
pip install lolcat
pip install --upgrade pip
pip3 install requests --upgrade
pip3 install requests[socks]
pip3 install stem
pip3 install instagram-py
cd $HOME
wget -O ~/instapy-config.json "https://git.io/v5DGy"
cd $HOME/Hack-OS
bash main/done.sh
