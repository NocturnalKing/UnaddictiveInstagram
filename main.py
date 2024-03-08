#import os
#import random
import getpass
#from time import sleep
from instagrapi import Client

cl = Client()
username = input("Enter Username: ")
password = getpass.getpass("Enter Password: ")
cl.login(username, password)

#Confirmed login
print("Logged into account!")

temp = temp = input("""Type a letter for a specific action
a - get all of your account's information
b - undecided
c - undecided
Your input: """)
while temp not in ["a"]: #,"b","c"]
	print("Sorry but that wasn't a valid input")
	temp = input("""Type a letter for a specific action
a - get all of your account's information
b - undecided
c - undecided
Your input: """)
temp = temp.lower()
if temp == "a":
	print(cl.account_info().dict())
