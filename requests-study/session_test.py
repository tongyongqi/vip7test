import data as data
import requests
import username as username
#1。请求地址
urlstr1 = 'https://www.wanandroid.com/user/login'
urlstr = 'https://www.wanandroid.com/lg/todo/list/0'
datas= {'username':'tongyongqi','password':'tyq069822,.?'}
#访问登录后的接口 用session方式访问
s= requests.session()
r=s.post(url=urlstr1,data=datas)
#发送请求
r2=s.get(url=urlstr)
print(r2.status_code)
print(r2.text)







