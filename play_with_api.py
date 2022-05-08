import requests

# GET METHOD
response = requests.get('http://127.0.0.1:8000/library/')

dict_response = response.json()
print(dict_response[0])
print(dict_response[0]['book_name'])
print(response.status_code)
assert response.status_code == 200
# print(response.headers)
print(response.headers['Content-Type'])

# POST
addbook_response = requests.post('http://127.0.0.1:8000/library/', json=
{'isbn': 'ABC6', 'aisle': 1, 'book_name': 'Testing Fun Five'},
                                 headers={'Content-Type': 'application/json'})

print(addbook_response.json())
response_json = addbook_response.json()
print(addbook_response.status_code)
assert addbook_response.status_code == 201
book_id = response_json['id']

# DELETE
deletebook_response = requests.delete('http://127.0.0.1:8000/library/' + str(book_id),
                                      headers={'Content-Type': 'application/json'})
print(deletebook_response.status_code)
assert deletebook_response.status_code == 204
