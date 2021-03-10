import requests,json

urlstr = 'http://httpbin.org/post'
#字典类型参数
paylod = {'cont':'selenium+jemter+loadrunner','qq':'970975018'}
#接口文档要求传入json类型，需要进行转换
#方法1：dunms方法
#通过json.dumps方法将python字符串转换成json类型
paylod = json.dumps(paylod)

#2.发送请求
# r= requests.post(url=urlstr,data=paylod)
#方法2
r= requests.post(url=urlstr,data=paylod)


print(r.encoding)
#3获取结果
print(r.text)

#返回为json类型，即可以通过r.json方法查看结果
print(r.json())