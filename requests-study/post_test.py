import data as data
import requests

#1。请求地址
import username as username

urlstr1 = 'https://www.wanandroid.com/user/login'
# urlstr='https://www.wanandroid.com/lg/todo/list/0'
datas= {'username':'tongyongqi','password':'tyq069822,.?'}
# 2。发送请求
r = requests.post(url=urlstr1,data=datas)
print(r.status_code)
print(r.json())

#响应结果为res_result
res_result = r.json()

#r2=r.test    r.test输出为字符串
errCode = (res_result['errorCode'])
username = res_result['data']['username']

#响应断言
if errCode == 0 and username == datas['username']:
    print('登录成功')





# 3.输出响应结果
print(r.status_code)
print(r.text)