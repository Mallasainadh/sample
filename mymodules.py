'''def greetings(name):
    print("welcome",name)'''

'''a=4
b=8
print(a+b)

a=int(input("a value"))
b=int(input("b value"))
print(a+b)'''

details={"idnos":[10,20,30],
         "names":["sai","srinu","dinesh"],
         "marks":[50,60,70]}

'''if __name__=="__main__":
    a=[10,20,30,40,50]
    a.append("code")
    a.extend("code")
    print(a)'''

'''def dummy():
    if __name__=="__main__":
        print("this program is run as script")
    else:
        print("this program is run as module")
dummy()'''

#math module
'''import math
print(math.pi)
print(math.pi*4)
print(math.sqrt(2))
print(math.log(2))
print(math.tan(45))
print(math.cos(60))
print(math.sin(30))
print(math.pow(2,4))
print(math.ceil(6.9))
print(math.floor(3.11))'''

'''from math import pi,sqrt,log,tan
print(pi)
print(sqrt(4))
print(log(6))
print(tan(45))'''

#sys module

'''import sys
print(sys.version)
print(sys.path)'''

#os module
'''import os
print(os.path)
print(os.getcwd())
print(os.listdir())
print(os.chdir("C:\\Users\\Administrator\\Downloads"))
print(os.listdir())'''

#random module
'''import random
a=random.sample(range(10,40),40)
print(a)''' #error

#randint()
'''import random
a=random.randint(50,60)
print(a)'''

#coice()
'''import random
a=[10,40,50,60,70]
b=random.choice(a)
print(b)'''

#dice code
'''import random
while True:
    input("enter the roll of dice")
    a=random.randint(1,6)
    print(a)
    option=input("roll agian? (y/n)")
    if option=="y":
        continue
    elif option=="n":
        break
    else:
        print("invaild option")'''



 








