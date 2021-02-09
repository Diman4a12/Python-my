import requests


numbers = [928, 930, 996, 964, 966, 903, 938, 972, 914, 947, 949, 981, 983, 927, 991]
api_url = "http://numbersapi.com/{}/math?json=true"
params = {
    'found' : 'true'
}


for i in numbers:
    res = requests.get(f"http://numbersapi.com/{i}/math?json=true", params=params)
    answer = res.json()
    if answer['found'] == False:
        print('Boring')
    else:
        print('Interesting')