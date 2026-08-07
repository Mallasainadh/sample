#email automation

import random
import math
import smtplib

digits="0123456789"
OTP=""#empty string

for i in range(6):
     OTP+=digits[math.floor(random.random()*10)]
otp=OTP+"is your otp"
msg=otp

s=smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login("mallasainadh469@gmail.com","ysam xkkr clzz wxnw")
mailid=input("enter the emailid you want to send to:")
s.sendmail(user,mailid,msg)

while True:
    a=input("enter the otp")
    if a==OTP:
        print("otp is correct")
    else:
        print("otp is incorrect")
