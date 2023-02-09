import requests

data = {"key1": "value1", "key2": "value2"}

response = requests.post("https://www.example.com/api/post_data", data=data)

print(response.status_code)
print(response.text)
