import requests



#1。请求地址
# urlstr = 'https://www.wanandroid.com/article/query'
urlstr = 'https://www.baidu.com/'
# 2。发送请求
param = {'k':'android'}
r=requests.get(url=urlstr,params=param)
# 3.输出响应结果
print(r.encoding)
print(r.status_code)
# print(r.text)