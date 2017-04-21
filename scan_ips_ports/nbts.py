#-*- coding: UTF-8 -*-
import os

file_object = open('res.txt')
try:
     all_the_text = file_object.read( )
finally:
     file_object.close( )

os.system('echo begin > nbtsres.txt')

for ip in all_the_text.split(':445\n'):
    os.system('echo '+ip+' >> nbtsres.txt')
    os.system(os.getcwd() + '\\nbtscan.exe '+ip + ' >> nbtsres.txt')
