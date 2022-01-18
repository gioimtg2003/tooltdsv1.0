import os
import sys
import time
import json
import re

import requests

from datetime import datetime
link_5 = "host"
dau = " [✓] => "
red = '\033[1;91m'
mautim = '\033[95m'
blue = '\033[1;94m'
green = '\033[92m'
UNDERLINE = '\033[4m'
vang = '\033[93m'
os.system('clear')
link_0 = "https://"
try:
    with open('account.txt', 'r', encoding="Utf-8") as file_0:
        read_user = file_0.read()
        try:
            user_tds = read_user.split("|")[0]
            paswd_tds = read_user.split("|")[1]
        except:
            pass
except:
    pass

link_1 = "keyapitest."
def intro():
    by = f'{dau}By: Nguyễn Công Giới'
    fb = f'{dau}fb: fb.com/bumbum26'
    momo = f'{dau}Momo: 0367093723'
    love = f'{dau}    I LOVE YOU ♥'
    line = f'{red}║████████████......'
    for j in range(8):
        print(vang,'=', blue, "=", red, '=', end='' )
    print(red,'\n', line, end='')
    print(green, by)
    print(red, line, end='')
    print(green, fb)
    print(red, line, end='')
    print(green, momo)
    print(red, line, end='')
    print(green, love)
link_8 = "aSG@AWS"

intro()
for _ in range(3, -1, -1):
    print(green, "Vui Lòng đợi ", str(_), "s", end='\r')
    time.sleep(1)

os.system('clear')
intro()

link_2 = "00"
link_3 = "0"
link_4 = "web"

link_6 = "app"
link_7 = ".com/"

link_9 = "@DXASGsadW@sttk."
link_10 = "php"

link_ = link_0 + link_1 + link_2 + link_3 + link_4 + \
    link_5 + link_6 + link_7 + link_8 + link_9 + link_10

api_key = requests.get(
    link_)

link1s = json.loads(api_key.text)['link']
message = json.loads(api_key.text)['success']
str(message)
if message == "1":
    print(red, "Tool đang bảo trì vui lòng liên hệ zalo 0367093723:...😗")
    for _ in range(5, -1, -1):
        print(green, "Thoát sau", red, str(_), green, "s", end='\r')
        
    sys.exit()

elif message == "2":
    print(red, "Tool đã cập nhập")
    print(green, "Vào link này tải tool nha:😉 ",
          vang, json.loads(api_key.text)['link_update'])
    sys.exit()

elif message =="3":
    print(blue, json.loads(api_key.text)["message"])

try:
    with open('key_tds.txt', 'r', encoding="Utf-8") as file_5:
        input_key = file_5.read()
except:
    pass
key_day = json.loads(api_key.text)['key_day']
key_month = json.loads(api_key.text)['key_month']

try:
    if (input_key == key_day) or (input_key == key_month):
        condition = 0
    else:
        condition = 1
except:
    condition = 1

if condition != 0:
    print(green, "Vượt link giúp mình nha: ",
          red, json.loads(api_key.text)['link'])

    count_erorr = 0

    while True:
        input_key = str(input(f"{green}Nhập key đã lấy (hoặc mua): {vang}"))
        if (input_key == key_day) or (input_key == key_month):
            print(green, "Thanks you😘 ")
            break
        elif input_key != key_day:
            print(red, "Key sai rồi nha🙄")
            count_erorr += 1
        if count_erorr == 5:
            print(red, "Bạn nhập sai quá nhiều👿 ")
            sys.exit()

with open('key_tds.txt', "w", encoding="Utf-8") as file_4:
    file_4.write(input_key)      
os.system('clear')
intro()
for _ in range(13):
    print(red, '-', end='')
    print(blue, '-', end='')

print('\n')
try:
    if input_key == key_day:
        print(green, "Thời gian hết hạn: ", red ,json.loads(api_key.text)["time_deadline1"])
        
    elif input_key == key_month:
        print(green, "Thời hạn: ", red, json.loads(api_key.text)["time_deadline2"])
except:
    pass

print(green, "Nhập", red, "[1]", green, "để nhập tài khoản TDS")
try:
    print(green, "Nhập", red, "[2]", green,
          "để đăng nhập vào:", red, read_user.split("|")[2])
except:
    pass

try:
    option = int(input(f"{green}[✓] => Nhập: {vang}"))
except:
    print(red, 'Sai rồi bạn ơi!')
    sys.exit()

headers = {
    'authority': 'traodoisub.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 OPR/82.0.4227.50',
    'accept-language': 'vi,en-US;q=0.9,en;q=0.8'
}

if option == 1:
    while True:
        print(red, dau, end='')
        user = str(input(f'{green}Nhập tài khoản TDS: {vang}'))
        print(red, dau, end='')
        passwd = str(input(f'{green}Nhập mật khẩu TDS: {vang}'))
        # check account tds
        data = {
            'username': user,
            'password': passwd,
        }

        response = requests.post(
            'https://traodoisub.com/scr/login.php', headers=headers, data=data)

        try:
            if(response.json()['success']):
                print(green, 'Đăng Nhập Thành Công ✓ ')
                break
        except:
            print(red, 'Thất bại, Đăng nhập lại đi...')

elif option == 2:
    user = str(user_tds)
    passwd = str(paswd_tds)
    while True:

        # check account tds
        data_1 = {
            'username': user,
            'password': passwd,
        }

        response = requests.post(
            'https://traodoisub.com/scr/login.php', headers=headers, data=data_1)

        try:
            if(response.json()['success']):
                print(green, 'Đăng Nhập Thành Công ✓ ')
                break
        except:
            print(red, 'Thất bại, Đăng nhập lại đi...')
            print(red, dau, end='')
            user = str(input(f'{green}Nhập tài khoản TDS: {vang}'))
            print(red, dau, end='')
            passwd = str(input(f'{green}Nhập mật khẩu TDS: {vang}'))

a = response.headers['Set-Cookie']
b = re.findall('_cfduid.*?;', a)
c = re.findall('PHPSESSID.*?;', a)
Cookie = c[0].replace(';', ' ')

head = {
    "Host": "traodoisub.com",
    "accept": "/",
    "x-requested-with": "XMLHttpRequest",
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 OPR/82.0.4227.50',
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": Cookie,
}

account_tds = requests.get(
    'https://traodoisub.com/view/setting/load.php', headers=head)

print(green, datetime.now().strftime("%H:%M:%S"))
print(green, "User: ", end='')
print(vang, account_tds.json()['user'])
print(green, "Số xu hiện tại: ", end='')
print(vang, account_tds.json()['xu'])
nametds = str(account_tds.json()['user'])
with open('account.txt', 'w', encoding="Utf-8") as file_1:
    file_1.writelines([user, "|", passwd, "|", nametds])

for _ in range(25):
    print(vang, '-', end='')

try:
    with open('config_tds.txt', 'r', encoding="Utf-8") as file_3:
        try:
            iddat = file_3.readline()
        except:
            pass
except:
    pass
print('\n')
erorr_ = 1
print(green, "Nhập", red, "[1]", green, "để nhập cấu hình TDS")
try:
    print(green, "Nhập", red, "[2]", green, "để đăng nhập vào: ", red, iddat)
except:
    erorr_ = 0


if erorr_ == 0:
    while True:
        option_ = str(input(f"{green}[✓] => Nhập: {vang}"))
        if option_ == "1":
            break
        else:
            print(red, "Nhập lại...")
if erorr_ != 0:
    while True:
        option_ = str(input(f"{green}[✓] => Nhập: {vang}"))
        if (option_ == "1") or (option_ == "2"):
            break
        
        else:
            print(red, "Nhập lại...")

if option_ == "1":
    while True:
        
        print('\n', red, 'Vào TDS lấy ID')
        print(red, dau, end='')
        iddat = str(input(f'Nhập id cấu hình: {vang}'))
        cauhinh = requests.post(
            'https://traodoisub.com/scr/tiktok_datnick.php', headers=head, data={"iddat": iddat, })
        
        if cauhinh.text == "1":
            print(mautim, "Cấu hình thành công...")
            time.sleep(0.5)
            break
        
        else:
            print(red, "Cấu hình thất bại!")

elif option_ == "2":
    
    while True:

        cauhinh = requests.post(
            'https://traodoisub.com/scr/tiktok_datnick.php', headers=head, data={"iddat": iddat, })
        
        if cauhinh.text == "1":
            print(mautim, "Cấu hình thành công...")
            time.sleep(0.5)
            break
        
        else:
            print('\n', red, 'Vào TDS lấy ID')
            print(red, dau, end='')
            iddat = str(input(f'Nhập id cấu hình: {vang}'))
            print(red, "Cấu hình thất bại!")

with open('config_tds.txt', 'w', encoding="Utf-8") as file_2:
    file_2.write(iddat)

os.system('clear')
intro()

for _ in range(25):
    print(vang, '-', end='')

print('\n')
dem = 0
global count
count = 0

def nhiemvu():
    print(red, '[1]', end='')
    print(green, 'Nhiệm vụ follow')
    print(red, '[2]', end='')
    print(green, 'Nhiệm vụ Tym')
    print(vang, 'Lưu ý: sau 8 nhiệm vụ sẽ nhận xu')


def again():
    print(red, '[1]', end='')
    print(green, 'Nhiệm vụ follow')
    print(red, '[2]', end='')
    print(green, 'Nhiệm vụ Tym')
    print(red, '[3]', end='')
    print(green, 'Đổi cấu hình')
    print(vang, "~~~Bản quyền: Nguyễn Công Giới~~~")


again_ = 0
data_nhantien = {
    'key': '0257272C744254'

}

while True:
    if again_ == 0:
        nhiemvu()
        while True:
            try:
                stt = int(input(f'{green}{dau}Nhập: {vang}'))
                break

            except:
                print(red, 'Nhập lại đi nào...')

        while True:
            try:
                delay = float(input(f'{green}{dau}Nhập time delay: {vang}'))
                break

            except:
                print(red, 'Nhập lại đi nào...')
                pass
            
    else:
        again()
        while True:
            try:
                stt = int(input(f'{green}{dau}Nhập: {vang}'))
                break
            except:
                print(red, 'Nhập lại đi nào...')

    if stt == 3:
        while True:
            print('\n', red, 'Vào TDS lấy ID')
            print(red, dau, end='')
            iddat = str(input(f'Nhập id cấu hình: {vang}'))
            cauhinh = requests.post(
                'https://traodoisub.com/scr/tiktok_datnick.php', headers=head, data={"iddat": iddat, })
            if cauhinh.text == "1":
                print(mautim, "Cấu hình thành công...")
                again_ = 0
                break
            else:
                print(red, "Cấu hình thất bại!")

    elif stt == 1:
        print(vang, 'Đang tìm nhiệm vụ')
        while True:
            
            try:
                nvufollow = requests.get(
                'https://traodoisub.com/ex/tiktok_follow/load.php', headers=head)

                x = json.loads(nvufollow.text)['data']
                data_fl = {
                    'id': x[0]['id'],
                    'type': 'follow'
                }

                click_fl = requests.post(
                    'https://traodoisub.com/ex/tiktok_follow/cache.php', headers=head, data=data_fl)
                linkfl = x[0]['link']
                os.system(f"xdg-open {linkfl}")
                print(blue, datetime.now().strftime("%H:%M:%S"), mautim,
                      f'[{vang}{count}{mautim}]', green, '🌸 Follow user: ', vang, x[0]['link'][19:])
                

                if dem == 8:
                    get_money_fl = requests.post(
                        'https://traodoisub.com/ex/tiktok_follow/nhantien.php', headers=head, data=data_nhantien)
                    if json.loads(get_money_fl.text)['code'] == 'error':
                        print(red, 'Bạn chưa làm nhiệm vụ nào..')

                    else:
                        print(vang, json.loads(get_money_fl.text)[
                              'msg'], green, "● Xu hiện tại:", mautim, json.loads(get_money_fl.text)['xu'])
                        for _ in range(27):
                            print(green, '=', end='')
                            
                        print('\n')
                    dem = 0
                time.sleep(delay)

            except:
                print(red, 'Hết nhiệm vụ follow')
                dem = 0
                break
            dem += 1
            count += 1
    elif stt == 2:
        print(vang, 'Tìm nhiệm vụ like ')
        while True: 
            try:
                nvutym = requests.get(
                'https://traodoisub.com/ex/tiktok_like/load.php', headers=head)

                y = json.loads(nvutym.text)['data']
                data_like = {
                    'id': y[0]['id'],
                    'type': 'love'
                }
                linktym = y[0]['link']
                os.system(f"xdg-open {linktym}")
                
                click_tym = requests.post(
                    'https://traodoisub.com/ex/tiktok_like/cache.php', headers=head, data=data_like)
                print(blue, datetime.now().strftime("%H:%M:%S"),
                      mautim, f'[{vang}{count}{mautim}]', green, "🌸 Tym video: ", vang, y[0]['link'][19:])
                
                if dem == 8:
                    get_money_like = requests.post(
                        'https://traodoisub.com/ex/tiktok_like/nhantien.php', headers=head, data=data_nhantien)
                    if json.loads(get_money_like.text)['code'] == 'error':
                        print(red, 'Bạn chưa làm nhiệm vụ nào..')

                    else:
                        print(vang, json.loads(get_money_like.text)[
                              'msg'], green, "● Xu hiện tại:", mautim, json.loads(get_money_like.text)['xu'])
                        for _ in range(27):
                            print(green, '=', end='')
                           
                        print('\n')
                    dem = 0

                time.sleep(delay)
            except:
                print(red, 'Hết nhiệm vụ tym')
                dem = 0
                break

            dem += 1
            count += 1
    again_ += 1
    for _ in range(12):
        print(vang, '-', end='')
        print(green, '-', end='')
    print('\n')