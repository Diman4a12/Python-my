import requests
a = []
a+=requests.get('https://stepic.org/media/attachments/course67/3.6.2/983.txt').text
c = a.count('\n')
print(c)