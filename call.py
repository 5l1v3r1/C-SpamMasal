#/usr/bin/python
# Thanks To Aylward Hxr
# (c) Hax28dh8Sec
# modif by KANG-NEWBIE


def spam():
	import os, time
	import subprocess as sp
	time.sleep(1)
	os.system('clear')
	print("\033[1;33m[!] Please Wait...")
	sp.call('pip install requests', shell=True, stdout=sp.DEVNULL, stderr=sp.STDOUT)
	import requests

	os.system("clear")
	print("""
\033[1;32m+---------------------------------------+
\033[1;32m|\033[1;31m          SPAM TELEPON MASAL           \033[1;32m|
\033[1;32m|\033[1;37m  CREATE BY WIDHISEC ft. KANG-NEWBIE   \033[1;32m|
\033[1;32m+---------------------------------------+
(*) Ketik Enter Untuk Melewati Step""")
	no1 =input("Masukkan Nomor Telepon1 =>")
	no2 =input("Masukkan Nomor Telepon2 =>")
	no3 =input("Masukkan Nomor Telepon3 =>")
	no4 =input("Masukkan Nomor Telepon4 =>")
	no5 =input("Masukkan Nomor Telepon5 =>")
	print("[-] STATUS:")
	r1 = requests.get('https://0x.nakocoders.org/rest-api/lain-nya/api.php?nomor='+no1)
	print("[+] SPAM1",r1.json()["msg"])
	r2 = requests.get('https://0x.nakocoders.org/rest-api/lain-nya/api.php?nomor='+no2)
	print("[+] SPAM2",r2.json()["msg"])
	r3 = requests.get('https://0x.nakocoders.org/rest-api/lain-nya/api.php?nomor='+no3)
	print("[+] SPAM3",r3.json()["msg"])
	r4 = requests.get('https://0x.nakocoders.org/rest-api/lain-nya/api.php?nomor='+no4)
	print("[+] SPAM4",r4.json()["msg"])
	r5 = requests.get('https://0x.nakocoders.org/rest-api/lain-nya/api.php?nomor='+no5)
	print("[+] SPAM5",r5.json()["msg"])


print()
buriq = ("dih mukon!!")
jeleq = ("nyadar juga elu ya babyk")
tanya = input("kamu ganteng? (jelas/ngak) ")
if tanya == 'jelas':
        print(buriq), spam()
elif tanya == 'ngak':
        print(jeleq), spam()
else:
        exit("ngetik yang bener goblok!!\n")
print()

pilih = input("lagi ngak cok (y/n) ")
if pilih == 'y':
	spam()
elif pilih == 'n':
	exit("oke deh sampai jumpa lagi beb:*\n")
else:
	exit("anda buntung ya?\n")
