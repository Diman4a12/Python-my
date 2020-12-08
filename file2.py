import requests
a = requests.get('https://stepic.org/media/attachments/course67/3.6.3/699991.txt').text
print(a)
while 'we' not in a:
    c = 'https://stepic.org/media/attachments/course67/3.6.3/' + str(a)
    b = requests.get(c).text
    print(c)
    a = b
    print(a)
else:
    print(a)