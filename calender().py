#calender module
'''import calender
year=2026
month=8
print(calender.month(year,month))'''

#year
'''import calender
year=2027
print(calender.calender(year))'''

'''import calendar
year=int(input("enter the year"))
print(calender.calendar(year))'''

'''a=int(input("enter the year"))
b=int(input("enter the month"))
print("calender.month(year,month")'''

#date and time
'''from datetime import date
a=date.today()
print(a)'''

'''import datetime
a=datetime.datetime.now()
print(a)'''

'''import timea=time.time()
print(a) #epoch time

b=time.localtime(a)
print(b)

print(f"today date is{b.tm_mday}-{b.tm_mon}-{b.tm._year}")'''

'''print(f"time is {b.tm_hour}:{b.tm_min}:{b.tm_sec}")

print(f"day is {b.tm_mday}-{b.tm_yday}-{b.tm_isdst}")'''

'''import random
import time
for i in range(10):
    a=random.randint(1000,9999)
    print(a)
    time.sleep(2)'''

#error handling
#syntax error-> compile error
#run_time error-> during excecution time it will happens
#logical error-> error is logical cant be visible

#syntax error
'''for i in range(10)
print(i)'''

#run_time error
'''a=int(input())
b=int(input())
print(a//b)'''#10/0->zero division error

#logical error
'''a=10
b=20
print(a-b)'''

'''a=10
b=20
if a<b:
    print("less")'''

'''a=10
b=20
if a>b:
    print("big")'''


