import requests

response = requests.post(
    'http://127.0.0.1:5000/advs/',
    json={
        'header': 'New Adv: sell moped',
        'owner': 'not me',
        'description': 'just posted an ad'
    })

print(response.headers)
print(response.text)

response = requests.get('http://127.0.0.1:5000/advs/1')

print(response.headers)
print(response.text)

response = requests.delete('http://127.0.0.1:5000/advs/1')

print(response.headers)
print(response.text)
