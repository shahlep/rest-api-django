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

# GET By id
response1 = requests.get('http://127.0.0.1:8000/library/' + str(book_id))

dict_response1 = response1.json()

print(response1.status_code)

assert response1.status_code == 200

print(dict_response1)

# PUT
response2 = requests.put('http://127.0.0.1:8000/library/' + str(book_id), json=
{'isbn': 'ABC8', 'aisle': 1, 'book_name': 'Testing Fun Seven'},
                          headers={'Content-Type': 'application/json'})

dict_response2 = response2.json()

print(response2.status_code)

assert response2.status_code == 200

print(dict_response2)

# GET By id
response3 = requests.get('http://127.0.0.1:8000/library/' + str(book_id))

dict_response3 = response3.json()

print(response3.status_code)

assert response3.status_code == 200
print(dict_response3)


# DELETE
deletebook_response = requests.delete('http://127.0.0.1:8000/library/' + str(book_id),
                                      headers={'Content-Type': 'application/json'})
print(deletebook_response.status_code)
assert deletebook_response.status_code == 204
