import requests

# truyền vào url website mình muốn thao tác
url = 'https://api.github.com/events'

r = requests.get(url=url)

# trạng thái truy cập trả về
#  200 thì trang web truy cập ổn định
# trả về 400 thì trang web ko thể truy cập
status = r.json

# lấy dữ liệu dạng json, json() là 1 kiểu dữ  liệu trong javascript
# ở đây là lấy ra actor của người đăng kí github mới nhất
data = r.json()[0]['actor']

print(status)
print(data)
