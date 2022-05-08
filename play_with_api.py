import requests

response = requests.get('http://127.0.0.1:8000/library/')

dict_response = response.json()
print(dict_response[0])
print(dict_response[0]['book_name'])
print(response.status_code)
#print(response.headers)
print(response.headers['Content-Type'])


