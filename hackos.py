import os

atk = ('''\033[1;92m
	Choose attack type
	[1] Manual Attack
	[2] Auto Attack
	[0] Back
		
	: ''')

os.system("clear")
os.system("bash main/banner.sh")

cse = input('''
\033[1;92mChoose whatever you want to hack here :

\033[1;93m[1] \033[1;92mInstagram Hack
\033[1;93m[2] \033[1;92mFacebook Hack
\033[1;93m[3] \033[1;92mEmail Hack
\033[1;93m[4] \033[1;92mMy social media
\033[1;93m[5] \033[1;92mAbout
\033[1;93m[99] \033[1;92mExit

\033[1;93m==> \033[1;92m''')
	
if cse == "1":
	while True:
		os.system("clear")
		os.system("bash main/banner.sh")
		a = input(atk)
		if a == "1":
			os.system("clear")
			os.system("bash core/Imanual.sh")
			break
		elif a == "2":
			os.system("clear")
			os.system("bash core/Iauto.sh")
			break
		elif a == "0":
			os.system("python hackos.py")
			break
		else:
			print("Enter valid input")
elif cse == "2":
	while True:
		os.system("clear")
		os.system("bash main/banner.sh")
		b = input(atk)
		if b == "1":
			os.system("clear")
			os.system("python core/fmanual.py")
			break
		elif b == "2":
			os.system("clear")
			os.system("python core/fauto.py")
			break
		elif b == "0":
			os.system("python hackos.py")
			break
		else:
			print("try again")

elif cse == "3":
	while True:
		os.system("clear")
		os.system("bash main/banner.sh")
		c = input(atk)
		if c == "1":
			os.system("clear")
			os.system("python core/gmanual.py")
			break
		elif c == "2":
			os.system("clear")
			os.system("python core/gauto.py")
			break
		elif c == "0":
			os.system("python hackos.py")
			break
		else:
			print("try again")
elif cse == "4":
	while True:
		os.system("clear")
		os.system("bash main/banner.sh")
		social = input("""
		\033[1;93m[1] \033[1;92mFollow on Instagram
		\033[1;93m[2] \033[1;92mFollow on Github
		\033[1;93m[3] \033[1;92mSubscribe on YouTube
		\033[1;93m[0] \033[1;92mBack
		
		==> """)
		if social == "1":
			print("Ok, Opening my Instagram profile in your phone")
			os.system("sleep 1.5")
			os.system("termux-open-url https://instagram.com/hackerx30/")
			os.system("python hackos.py")
			break
		elif social == "2":
			print("Ok, Opening my Github profile in your phone")
			os.system("sleep 1.5")
			os.system("termux-open-url https://github.com/MrHacker-X/")
			os.system("python hackos.py")
			break
		elif social == "3":
			print("Ok, Opening my YouTube channel in your phone")
			os.system("sleep 1.5")
			os.system("termux-open-url https://youtube.com/channel/UC2t1smKARnlzoqELbyEhXVw")
			os.system("python hackos.py")
			break
		elif social == "0":
			os.system("python hackos.py")
			break
		else:
			print("Enter correct number")
		

elif cse == "5":
	os.system("clear")
	os.system("bash main/banner.sh")
	print()
	os.system("python main/about.py")
	
elif cse == "99":
	print("\033[1;92mok, as you wish\nYou're exiting..... ")
	os.system("sleep 2.0")

else:
	os.system("python hackos.py")
