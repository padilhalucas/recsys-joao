import requests
text = 'X-men'
value = requests.get('https://recsys-joao.herokuapp.com/movie?title=text')
print(value)