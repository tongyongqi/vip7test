#1。定义一个类
class washer():
    #初始化功能参数
    def __init__(self,width,height):
        #添加参数
        # self.width=200
        # self.height=400
        self.width=width
        self.height=height
    #方法
    def wash(self):
        print('我会洗衣服')
    def print_info(self):
        print(f'heier1的宽度是:{self.width}')
        print(f'heier1的高度是:{self.height}')
#2。创建对象-----实力化
heier1= washer(300,400)
# print(heier1)
# heier1.wash()
# heier2 = washer()
# print(heier2)
# heier1.width = 500
# heier1.height= 800
# print(f'heier1的宽度是:{heier1.width}')

# print(f'heier1的高度是:{heier1.height}')
heier1.print_info()