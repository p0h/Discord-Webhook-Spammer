from dhooks import Webhook
import os 
import time
import colorama
import requests
from colorama import Fore

RESET = Fore.RESET
CYAN = Fore.CYAN

main = 'mode 75,25'
os.system(main)

os.system("title [-github.com/p0h-] - Discord Webhook Spammer")

def Main():
	print(f"""

   {CYAN}╦ ╦╔═╗╔╗ ╦ ╦╔═╗╔═╗╦╔═  ╔═╗╔═╗╔═╗╔╦╗╔╦╗╔═╗╦═╗	   {RESET}Scriptor {CYAN}~ {RESET}bad#7076
   {CYAN}║║║║╣ ╠╩╗╠═╣║ ║║ ║╠╩╗  ╚═╗╠═╝╠═╣║║║║║║║╣ ╠╦╝
   {CYAN}╚╩╝╚═╝╚═╝╩ ╩╚═╝╚═╝╩ ╩  ╚═╝╩  ╩ ╩╩ ╩╩ ╩╚═╝╩╚═	   {RESET}Version {CYAN}~ {RESET}1.0


            {CYAN}╔═══════════════════════════════════════════════╗
    	    {CYAN}║ {RESET}[{CYAN}1{RESET}] Unlimited Spam (Until Script Closed)      {CYAN}║
	    {CYAN}║ {RESET}[{CYAN}2{RESET}] Advanced Spam (Pick amount of times)      {CYAN}║
            {CYAN}╚═══════════════════════════════════════════════╝

	""")
	hookurl = input(f"{RESET}[{CYAN}>{RESET}] Enter webhook link : ")
	data = input(f"{RESET}[{CYAN}?{RESET}] Enter the data you would like to send : ")

	hook = Webhook(f'{hookurl}')

	choice = input(f"{RESET}[{CYAN}-{RESET}] Select option displayed in menu above : ")

	if choice == '1':
		while True:
			hook.send(f'{data}')
			print(f'{RESET}[{CYAN}!{RESET}] Sent request')

	if choice == '2':
		amount = int(input(f"{RESET}[{CYAN}?{RESET}] How many times do you want to send a request : "))
		for x in range(amount):
			hook.send(f'{data}')
			print(f'{RESET}[{CYAN}!{RESET}] Sent request')
		print(f"{RESET}[{CYAN}!{RESET}] Process finished sent {CYAN}{amount}{RESET} requests to webhook")
		time.sleep(5)

Main()