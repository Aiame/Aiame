#寫class 1.(第一個參數圓或正方形,第二個參數周長or半徑)要算圓or正方形 告訴面積  2.給若干個圓周長，算出圓面積加總 3.順便再畫圖好了
# import numpy as np
# """
# np.random.seed(3)
# arr = np.random.randint(0,21,15)
# b = []
# print(arr)
# for i in arr :
#     if i%2 ==0:
#         b += arr
#         #b += arr[]
# print(b)
# """



#我要算圓or正方形並且告訴我面積  2.給若干個圓周長，並算出圓面積加總
import math
class P:
    global a 
    a = math.pi
    # def __init__(self, radius, length):
    #     self.length = length
    #     self.radius = radius
    def __init__(self,x, radius, length):
        if x==0:
            self.x = 1
        elif x==1:
            self.x = 0
        else:
            return None
        self.length = length
        self.radius = radius
    def area(self):
        if self.x == 1:
            return self.radius*self.radius*a
        else:
            return self.length*self.length

class C(P):
    def __init__(self):
        self
    def radiusum(self,x,y,z):
        i = [x,y,z]
        key = [eval('i**2*a') for i in i[:]]
        return sum(key) 
g = P(1,5,9)
print(g.area())
k = C()
print(k.radiusum(5,6,7))