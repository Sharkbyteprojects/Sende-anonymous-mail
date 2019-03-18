import requests
import time
froms = 'python-mailer@sharkbytenetwork.net'
print("Sharkbyteprojects Mailing Service Free")
to = "sharkbyteprojects@protonmail.com"
subject = "test send mail"
message = "travic ci test OK!"
url = 'http://services.sharkbyte.bplaced.net/send.php?user=python'
payload = {'from': froms,
'to': to,
'sub': subject,
'messages': message}
print(" ")
print(" ")
print("HTML CODE FROM ANSWER:")
files = {}
headers = {}
response = requests.request('POST', url, headers = headers, data = payload, allow_redirects=False)
print(response.text)
time.sleep(10)
