__author__ = 'Administrator'
import string
str = raw_input('Input a string:')
num_space = 0
num_letter = 0
num_digit = 0
for c in str:
    if c.isspace():
        num_space+=1
    elif c.isalpha():
        num_letter+=1
    elif c.isdigit():
        num_digit+=1
print('%d spaces, %d letters and %d digits' %(num_space, num_letter, num_digit))
