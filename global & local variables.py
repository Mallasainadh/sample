
#global and local variables
#first case of global variable
'''a=4
def check():
    print("inside value is",a)
check()
print("outside value is",a)'''

#second case of global variables
'''a=2
def check2():
    a=5
    a=a**2
    print("inside value is",a)
check2()
print("outside value is",a)'''

#third case of both global and local variables
'''a=6
def check3():
    a=8
    print("inside value is",a)
    a=10
    print("updated value is",a+5)
    b=13# local variable
    b=b+a
    print("value of b is",b)
check3()
print("a value is",a)
print("b value is",b)'''

#usage of global keyword
'''a=4
def final():
    global a,b
    print("inside value is",a)
    a=15
    print("update value is",a)
    #global b
    b=20
    b=b+a
    print("value of b is",b)
final()
print("a value is",a)
print("b value is",b)'''

#Attendence tracker
'''student=int(input("enter the total students"))
p=()
a=()
for i in range(1,students+1):
    attendence=input(f"student {i} present/absent")
    if attendence=="p":
        p+=1
    elif attendence=="a":
        a+=1
print("..........attendence report.........")
print("total students",students)
print("total presenties",p)
print("total absenties",a)'''
    
    
                      
        
    














