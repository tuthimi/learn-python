__author__ = 'Administrator'
yang = []
yang.append(1)
one = []
one.append(1)
temp = []
temp.append(1)
for i in range(10):
    if i==0:
        print(yang)
    elif i==1:
        yang.append(1)
        print(yang)
    else:
        yang.insert(0,1)
        for j in range(1,i,1):
            yang[j] = yang[j] + yang[j+1]
        print(yang)
