import random
import requests
import threading
import user_agent
from random import choice
from colorama import *


threads = 50
ftttt = requests.get("here put url where u have the ids name").text.splitlines()
logo = f'{Fore.CYAN}Solo.to {Fore.MAGENTA}Checker '
print(logo)


def claim_user():
    while True:
     with open("solo_to.txt", "r") as f:
      user = choice(f.readlines()).strip()
     r = requests.get('https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1')
     lmao = r.json()
     emails = lmao[0]
     cookies = {
    'cf_clearance': 'flHMr6U47_3NT.vN2wsLTz5yzrpTxYTPyah3uroNgMQ-1660961555-0-150',
    '_fbp': 'fb.1.1660961556684.64289074',
    'XSRF-TOKEN': 'eyJpdiI6IjZ0bVk3VmtYdTArNnhqSzRPZmRaNXc9PSIsInZhbHVlIjoiV0JzdDFaQ25FSFFjcFJqTTUzSHpzSWQvSlJUZVNsdkFzWEpTUW9HZWdGL3lWRGpEdlRXN0lGSFZiQ2Z3YWtMMVAyQlQvMDVaNmZHc0hFMXcyL05CeFlXRy9TcVpHNkFXaGttNnFGaDZudHUrMlJuN3RSeG8rbDJTNzRPb1QrWVUiLCJtYWMiOiJhMWIyZjhiMGVlODhiZjUxNTFiZGUyNDQ2NzBmMDllYjljMGI1MmQwMmI2MWMxOWMwZTlkOGJlNTkwNTk5MGY3IiwidGFnIjoiIn0%3D',
    'soloto_session': 'eyJpdiI6IlBQSFBKY2l0OHdPd0huRkkwbnBKbkE9PSIsInZhbHVlIjoicURYQlg0Y2U1a3FBV1dCT3pUNVhsaThTOCt0alNSUzRiN1l3YVpPTC95dW9zRm5zTi93S3ZoczRLakxXck1NQjY2a2h1Tys0RUxIVTk3RjdpVmhWRHltTVM4dnlNWUtVZFVnZ1VSYnJoY3l2a0dVcHR3Vm1WUjZaTnVhQ2w5MysiLCJtYWMiOiI0NzI3NWEyNjQzMDEwZmQ1ZGMzYThjM2E5ZDA1MWU0YmUyNDdhM2FmMTJiMGMwMjE5NDBmNDA0ZTE3Mjk2YWZmIiwidGFnIjoiIn0%3D',
}

     headers = {
    'authority': 'solo.to',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'origin': 'https://solo.to',
    'referer': f'https://solo.to/register/{user}',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Microsoft Edge";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': user_agent.generate_user_agent()
}

     data = {
    '_token': 'Ddjzs3qh8icHPZiXCVlt3Qh8050OxI6S84iG8ZJ5',
    'username': user,
    'email': emails,
    'password': ':2DP!zaTiLaCBw9',
    'password_confirmation': ':2DP!zaTiLaCBw9',
    'g-recaptcha-response': '03ANYolqtAeyvmmjlPNsRVooB57habd3522xnj-fo8i935kj6tqYMjcxPbzLPnsLcZLiokF9N93o1Ap9VsSh-vJyznwv65B2ShtFWWS3g_c_gXCx_NJr70ECj4Ju9Q-hc1tzCZH1KrVMs7jDUJ3YImv9j3Ozn6Mo-RJq7tPRJUNFqUSCE7-17tQAbjETy06lUnWXv1os3zxf1vSA-lg65YdmrhYi1lYtrjhXXOml6iB-o5KM8-Df9TYJfxUt4NLXitQsqp-38qnhyJ_vLFZQI4ulTlbxPrb2EOyH8zCGC8XgjTsnDZ_d71JhCij__6nEyW-fYIcDb6-RGko5v3MeF9NzDzBe1uO3f9k63D-BXv-nk1e_FyxqoRSeMnj5b-vWgYl-YV3OGNY-odSdBCZjl0J2nDRe5ulLbXkVJus9xn5xMlRPY7WCThKiHKzqU9OGAkvVi-NH6e5aA24OVd9eBRPR-t0D06ng2bJ-ZjYIo1H9JYNpsxT2kceTpVNfz48grX1PeQGPfTZ7JXOEaLYKUhJd_nQyepMmBU9Uf2H-_3XwMD5s5v0GHhmJoqVL9Xccd6EB-Alx8LD66L',
}

     r = requests.post('https://solo.to/register', cookies=cookies, headers=headers, data=data)
     if f'solo.to/{user}' in r.text:
        print(f'{user} claimed!')

def check_link():
    while True:
        link = random.choice(ftttt)
        cookies = {
            'XSRF-TOKEN': 'eyJpdiI6IllrZXh5aGIvcGpwWXZTclpnNExJYkE9PSIsInZhbHVlIjoia3RPdDVoZG5vR1lESTQ3ZnB5dWl5UldkbXRGaDl4emZvajBVbHhaT3NOZGpsajdham9OcGhSaFcvQjZFL1RhNmFjS2d4T0NUMWFPN1B4akVaVmViei9BNkgzL0RCUVcybHVIa09QR3NuOGNFTDBocTBIa0VjakFhMzFqelhJVloiLCJtYWMiOiI5Y2MyNTQ5NjQxZTI1NDFkZjg2MTM1MGFlNGI4OWNlMzliY2YxMjIzMGIyZjljNTY5OGM5NWIyNzk1MDM1Y2UyIiwidGFnIjoiIn0%3D',
            'soloto_session': 'eyJpdiI6IlZTSXYwclNKYWVESTNURE0xYmpBMlE9PSIsInZhbHVlIjoiVS9GOFF0b09SS2tqa3JaRDVQZ1JZMWlVaVdaWm8xZEdEa3ZXSDZ0WGVZUktDSE4wZnZQOHFEaXVSakgxRkpEQ01ORVpiN0dLdm5ST08zRDZvdUhxZnNCU3Rsc0lIanpuVG1BVHZ4WDJMVk9pWUhweVM3bmdBdG1pZFROY29lYy8iLCJtYWMiOiIwYTA4ODI1NWI0ZGE2NWRhZWUyZjczOWIzOWI2YzExYTIzNWU2YjcxYTljOGEzMDgyYjFiNjVhNWVlMzZmYWVmIiwidGFnIjoiIn0%3D',
        }
        
        headers = {
            'authority': 'solo.to',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Microsoft Edge";v="104"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': user_agent.generate_user_agent()
        }
        r = requests.get(f'https://solo.to/{link}', cookies=cookies, headers=headers)
        if f'profile-name' in r.text:
         print(f'{Fore.RED}{link} is taken!')
        if 'The page' in r.text:
         print(f'{Fore.GREEN}{link} is avail!')
         open("solo_to.txt", "a").write(f'{link}\n')
         claim_user() # claim user function coming soon.


while True:
 if threading.active_count() < int(threads):
         threading.Thread(target=check_link).start()
