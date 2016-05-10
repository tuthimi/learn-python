__author__ = 'Administrator'
l=[]

for i in range(3):
    temp = int(raw_input("Input the %dth number:" %i)) #加int()进行类型转换，否则会按字符串进行排序
    l.append(temp)

l.sort()
print(l)