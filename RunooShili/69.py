# -*- coding: UTF-8 -*-
__author__ = 'Administrator'
n=11
count = 0

line  = [i+1 for i in range(n)]
j = 1
i = 0
while len(line) > 1:
    if i == len(line):
        i = 0
    if j%3 ==0:
        del line[i] #list数组的remove，del与pop
        i=i-1
        print(line)
        #print(i,j)
    i=i+1
    j=j+1




