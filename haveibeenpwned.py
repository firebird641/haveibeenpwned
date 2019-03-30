#!/usr/bin/python

import hashlib,requests,getpass

print("Type in your password...")
pwd = getpass.getpass()

sha1pwd = hashlib.sha1(pwd.encode('utf-8')).hexdigest().upper()
head = sha1pwd[:5]

print("Processing...")
url = 'https://api.pwnedpasswords.com/range/' + head
res = requests.get(url)
if res.status_code != 200:
	print("Error")
else:
	output = res.text.splitlines()
found = 0
for x in output:
	if sha1pwd == head+x.split(":")[0]:
		print("Password has been found "+x.split(":")[1]+" times.")
		found = 1
if found == 0:
	print("Password is secure.")
