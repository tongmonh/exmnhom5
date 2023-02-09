import requests

# GET request
response = requests.get("https://www.example.com/api/get_data")
print(response.text)

# POST request
data = {"key": "value"}
response = requests.post("https://www.example.com/api/post_data", data=data)
print(response.text)

# PUT request
data = {"key": "new_value"}
response = requests.put("https://www.example.com/api/update_data", data=data)
print(response.text)

# DELETE request
response = requests.delete("https://www.example.com/api/delete_data")
print(response.text)
