import requests
# -*- coding:utf-8 -*-

payload = {'name' : 'hello xiao du', 'age' : 18}
res = requests.get('http://www.baidu.com', params=payload)
print(res)
print('*' * 50)
print(res.headers)
print(res.content)