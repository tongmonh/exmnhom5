import requests

# truyền vào url website mình muốn thao tác
url = 'https://api.ipify.org/'

r = requests.get(url=url)

# trạng thái truy cập trả về
#  200 thì trang web truy cập ổn định
# trả về 400 thì trang web ko thể truy cập
status = r.json


# lấy dữ liệu dạng văn bản
data = r.text

print(r.status_code)
print(status)
print(data)
