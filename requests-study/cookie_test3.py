import requests

#发送请求
urlstr = 'https://www.wanandroid.com/user/login'
data = {'username':'tongyongqi','password':'tyq069822,.?'}

#发送请求
r = requests.post(url=urlstr,data=data)
print('****',r.text)

print(r.cookies['JSESSIONID'])

#获取上次请求放回的response中的cookie，通过字典的形式引用cookie返回的jsessionin，放入下次请求cookoe中
cookie = {
    "JSESSIONID" : r.cookies['JSESSIONID']
}

#携带cookie发送请求
r2 = requests.get('https://www.wanandroid.com/lg/todo/list/0',cookies = cookie)

print("*****",r2.text)
print("*****",r2.headers)