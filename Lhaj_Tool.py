import requests
import socket
import random
import colorama

# matkarzch khtr ktbt bl english habibi.
# hardcoded username and password
username = "lhaj"
password = "instatool"

# ask user for input
user_input = input("Enter your username: ")
pass_input = input("Enter your password: ")

# check if username and password are correct
if user_input == username and pass_input == password:
    print("Access granted! Welcome To LHAJ Tool!")
else:
    print("Access denied.")

3
#colors
RED     = '\033[31m'
GREEN   = '\033[32m'
YELLOW  = '\033[33m'
BLUE    = '\033[34m'
MAGENTA = '\033[35m'
CYAN    = '\033[36m'
WHITE   = '\033[37m'
RESET   = '\033[39m'
id_tele = ('5105814026')
token_bot = ('6075118415:AAGLS0jGUQ4jfYy1liUEBxCaENijYbkkQRk')
def gethip():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    print(hostname)
    print(IPAddr)
def uch():
    ld = '\033[1;32m'
    f2 = '\033[1;35m'
    headers = {'HOST': 'www.instagram.com',
               'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) InspectBrowser',
               'X-CSRFToken': 'TNZhAQCH8OaoK8F5oZNHJ5ZrkAlSmcMM',
               'X-Instagram-AJAX': 'cec4fe0d7efe',
               'X-IG-App-ID': '936619743392459'
               }
    a7rf = ("qqeerrttyyuuiiooppllkkjjhhggffddssaazzxxccvvbbnn11223344556677889900....____")
    while True:
        user = str("".join(random.choice(a7rf) for i in range(5)))
        url = f'https://www.instagram.com/{user}/'
        rq = requests.get(url, headers=headers)
        if rq.status_code == 200:
            tlg = (
            f'https://api.telegram.org/bot{token_bot}/sendMessage?chat_id={id_tele}&text=\nuser insta :  @{user}\nBy Lhaj \nmy website : https://alhelfi.softr.app \nتنويه قد يكون اليوزر مبند ')
            req = requests.post(tlg)
            print('\033[1;36m' " user found :" + user)
        elif rq.status_code == 404:
            print('\x1b[2;31m' + " user not found : " + user)
def irep():
    rs = requests.session()
    nu, n = 0, 0
    username = input(f'\033[31m[+]\033[33m username : ')
    password = input(f'\033[31m[+]\033[33m password : ')
    Target = input(f'\033[31m[+]\033[33m target username : ')
    url = 'https://www.instagram.com/accounts/login/ajax/'
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
        'content-length': '275',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'csrftoken=DqBQgbH1p7xEAaettRA0nmApvVJTi1mR; ig_did=C3F0FA00-E82D-41C4-99E9-19345C41EEF2; mid=X8DW0gALAAEmlgpqxmIc4sSTEXE3; ig_nrcb=1',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36',
        'x-csrftoken': 'DqBQgbH1p7xEAaettRA0nmApvVJTi1mR',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': '0',
        'x-instagram-ajax': 'bc3d5af829ea',
        'x-requested-with': 'XMLHttpRequest'
    }
    data = {
        'username': f'{username}',
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:{password}',
        'queryParams': '{}',
        'optIntoOneTap': 'false'
    }
    r = rs.post(url, headers=headers, data=data)
    if 'authenticated":true' in r.text or 'userId' in r.text:
        rs.headers.update({'X-CSRFToken': r.cookies['csrftoken']})
        print(F'your user : ' + username)
        id = input(f'[+] target id : ')
        print('''
    \033[31m[01]\033[32m [>] spam
    \033[31m[02]\033[32m [>] violence
    \033[31m[03]\033[32m [>] Impersonation
    \033[31m[04]\033[32m [>] Sexual activity
    \033[31m[05]\033[32m [>] harassment
    \033[31m[06]\033[32m [>] Self-harm
    \033[31m[07]\033[32m [>]Hate on
    \033[31m[00]\033[32m [~] exit
        ''')
        xx = int(input(f"[+] choose number : "))
        if xx == 1:
            q = 1
        elif xx == 2:
            q = 5
        elif xx == 3:
            w = 8
        elif xx == 4:
            q = 4
        elif xx == 5:
            q = 7
        elif xx == 6:
            q = 2
        elif xx == 7:
            q = 6
        else:
            exit()
        P1 = int(input(f'\033[31m[+]\033[32m how many reports : '))
        tu = int(input(f'\033[31m[+]\033[32m delay : '))
        print('=' * 5 + 'start' + '=' * 5)
        for i_1 in range(P1):
            url_1 = f'https://www.instagram.com/users/{id}/report/'
            data_1 = {'source_name': '', 'reason_id': q, 'frx_context': ''}
            report_1 = rs.post(url_1, data=data_1)
            if '"status":"ok"' in report_1.text:
                nu += 1
            else:
                n += 1
            time.sleep(tu)
            print(f"\rDone={nu} | Error={n}", end="")

    else:
        print('[@] error login')
colorama.init()

print(colorama.Fore.RED + '''

 ██▓     ██░ ██  ▄▄▄       ▄▄▄██▀▀▀
▓██▒    ▓██░ ██▒▒████▄       ▒██   
▒██░    ▒██▀▀██░▒██  ▀█▄     ░██   
▒██░    ░▓█ ░██ ░██▄▄▄▄██ ▓██▄██▓  
░██████▒░▓█▒░██▓ ▓█   ▓██▒ ▓███▒   
░ ▒░▓  ░ ▒ ░░▒░▒ ▒▒   ▓▒█░ ▒▓▒▒░   
░ ░ ▒  ░ ▒ ░▒░ ░  ▒   ▒▒ ░ ▒ ░▒░   
  ░ ░    ░  ░░ ░  ░   ▒    ░ ░ ░   
    ░  ░ ░  ░  ░      ░  ░ ░   ░  
                                   

''')
                      
print(colorama.Fore.GREEN + 'Scripted By Lhaj Contact Me Discord : SIC3KNESS#9596')
print(''' 
[\] Here's the cmds list below, don't abuse.
[01]Show My Ip & Hostname

[02]uch

[03]about

[04]Report Insta

[05] User Info

''')
chinput = input('select number : ')
if chinput == '1':
    gethip()
elif chinput == '2':
    uch()
elif chinput == '3':
    print('''
    LHAJ 🇹🇳
    Insta Name : Hamda_souli
    BOT DEVELOPPER 💻
    CODER💻🔐
    ''')
elif chinput == '4':
	print('''
	[Uh-Oh][Service Currently Down]
	")
	
elif chinput == '5':
    print('''
    [User] Normal.
    [Limits] No Abuses.
    [Key] Premuim Key.
    [Days] 30 Day.
    ''')

    irep()

