__author__ = 'Administrator'

num = int(raw_input("How many fibnacci?"))
def fibnacci(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fibnacci(n-1)+fibnacci(n-2)

for i in range(num):
    print'%d, '%fibnacci(i+1), #print输出时不自动加换行的方法

