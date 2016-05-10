__author__ = 'Administrator'
year = int(raw_input("YEAR:\n"))
month = int(raw_input("MONTH:\n"))
day = int(raw_input("DAY:\n"))

months = (0,31,59,90,120,151,181,212,243,273,304,334)

if 1<=month<=12:
    sum = months[month-1]
else:
    print("MONTH input error!\n")

if 1<=day<=31:
    sum += day;
else:
    print("DAY input error!\n")

if ((year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)))and month>=2:
    sum += 1

print ("The day num is %d" %sum)