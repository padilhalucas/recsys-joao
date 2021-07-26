import requests
text = 'The hangover'
value = requests.get('https://recsys-joao.herokuapp.com/movie?title=' + str(text))
part = value.json()
print(part[0].get('Name'))
