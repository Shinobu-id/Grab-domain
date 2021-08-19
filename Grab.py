# Menganti nama author Tidak membuatmu menjadi orang yg kreatif 
#Coded by : Hudaxcode
#site : https://hudaxcode.xyz
import requests,time
import re
from IPython.display import clear_output
green = '\x1b[92m'
white = '\x1b[37m'
print('[!] Author : Hudaxcode ')
print('[!] Example: 2021-01-04')
date = input("[?] Input Date : ")
page = input('[?] Input Page : ')
print('')

def ok():
	time.sleep(1)
	print(f'[!] File saved ')
	print('[!] Thanks For use my Tools !')
def close():
	print(f'\n{white}[1] Filter Duplicat lane')
	print(f'{white}[2] Close')
	tod = input('[?] Select : ')
	tar = input('[?] Output : ')
	if tod =="2":
		print('[!] Thanks For use my Tools !')
		exit()
	if tod == "1":
		seen = set()
		with open('result.txt', 'r') as fin, open(tar, 'w') as fout:
			for line in fin:
				h = hash(line)
				if h not in seen:
					fout.write(line)
					seen.add(h)
			ok()
					

					
for page in range(1,int(page)):
    headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    req = requests.get('https://www.cubdomain.com/domains-registered-by-date/'+date+'/'+str(page), headers=headers).content.decode('utf-8')
    rex = re.findall('<a href="(.*?)">', req)

    for i in rex:
        if 'https://www.cubdomain.com/site/' in rex:
            pass
        elif 'tools' in i:
            pass
        elif 'domains' in i:
            pass
        elif 'javascript:;"' in i:
            pass
        elif 'dcounter.cubdom' in i:
            pass
        elif 'contact"' in i:
            pass 
        elif 'about"' in i:
            pass
        elif 'chrome.goo' in i:
            pass  
        elif 'er.com/inte' in i:
            pass
        elif 'facebook.com/cubdo' in i:
            pass
        elif 'rest.com/cub' in i:
            pass
        elif 'domain.com"' in i:
            pass
        elif 'domain.com/privacy-' in i:
            pass
        elif 'ain.com/terms-and' in i:
            pass
        elif 'in.com/cookies-po' in i:
            pass
        elif 'ain.com/disclaimer"' in i:
            pass
        elif 'in.com/l/interserver"' in i:
            pass
        else:
            rp = i.replace("https://www.cubdomain.com/site/","")
            clear_output(wait=True)
            print(f"{white}[!] {green}{rp}" ,end='', flush=True)
            result = open('result.txt', 'a').write(str(rp)+'\n')
close()

