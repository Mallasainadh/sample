#oops
#syntax
#class declaration

'''class classname():
    #attritude
    name="sai"
    age=23
    place="vja"
    def fname(method_name):
        print("statements")
a=classname()
a.fname()'''

#class declasration
'''class details():
    name="sai"
    age=23
    place="vja"
    def display (self):
        print(self.name,self.age,self.place)
a=details
print(dir(a))
a.display()'''

#object instantiaction
'''class details():
    def data(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
     print(self.name,self.age,self.place)
a=details()
print(dir(a))
a.data("satya",22,"vja")
a.display()
b=details()
b.data("veera",24,"vja")
b.display()'''

#constructor = _init_ or new = we can give the values directly in class
'''class Details():
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details(input("name"),input("age"),input("place"))
print(dir(a))
a.display()'''

'''class Details():
    #creating a constructor
    def __init__(self,name,age,place):
        self.name=input("name")
        self.age=int(input("age"))
        self.place=input("place")
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.display()'''

#diff b/w _ and __
'''class employee1():
    def __init__(self):
        self.name="sai"
        self._mailid="sainadh@gmail.com"
        self.__salary=10000#private variable
        class employee2():
     def __init__(self):
        self.name="srinu"
        self._mailid="srinivasarao@gmail.com"
        self.__salary=100000#private variable
a=employee1():
print(dir(a))
print(a.name)
print(a._mailid)
#print(a.__salary)
print(a._employeel__salary)
a=employee2()
print(dir(a))
print(b.name)
print(b._mailid)
#print(b.__salary)
print(b.employee2__salary)'''

#operator overloading

'''a=2;b=4
print(a+b)
print(a.__add__(b))
print(a.__add__(5))
print(a.__sub__(1))
print(a.__mul__(2))
print(a.__pow__(2))
#print(a.__div__(2))
print(a.__ge__(7))
print(a.__le__(10))
print(a.__eq__(2))
a=[2,3,4,5,6,7,8];b=[4,5,6,7,8,9,10]
print(a+b)
print(a.__add__(b))
print(a.__getitem__(2))
print(a.__getitem__(5))
a="code";b="gnan"
print(a+b)
print(a.__add__(b))
a="python";b="course"
print(a.__add__(" "+b).title())
print("sai".__add__("mr"))'''

#operating overraiding
'''
class A():
    def __init__(self,a):
        self,a=a
    def __add__(self,value):
        return self.a*value.b
class  B():
    def __init__(self,b):
        self.b=b
x=A(5)
y=B(4)
#x=5
#Y=4
print(x+y)'''

#method overloading
'''class new():
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("the sum is",a+b+c)
        elif a!=None and b!=None:
            print("the product is",a*b)
        else:
            print("program ends")
a=new()
a.sum()
a.sum(2,4,6)
a.sum(6,3)'''

#method overriding
'''class Animal():
    def speak(self):
        print("animals can make sounds")
class Dog():
    def speak(self):
        print("dog barks")
a=Animal()
b=Dog()
a.speak()
b.speak()'''


'''class car():
    def vehicle(self):
        print("Thar")
class bike():
    def vehicle(self):
        print("vespa")
a=car()
b=bike()
a.vehicle()
b.vehicle()'''

#single inheritance
'''class RBI():#parent class
    cash=100000
    def available_cash(cls):
        #print("available_cash is",cls.cash)
        print("available_cash is",RBI.cash)
class SBI(RBI):#child-1
    pass
class HDFC(RBI):#child-2
    cash=50000
    def new_cash(cls):
        #print("new cash is",cls.cash+cls.cash)
        print("new cash is",cls.cash+RBI.cash)
a=HDFC()
a.available_cash()
a.new_cash()'''

#multiple-inheritance
'''class father():
    def height(self):
       print("height is 5.5 inches")
class mother():
    def weight(self):
        print("weight is 60kgs")
class kid():
    def dob(self):
        print("just born....")
a=father()
b=mother()
c=kid()
a.height()
b.weight()
c.dob()'''

#multi-level-inheritance
'''class grandparent():
    def land(self):
        print("10 acres")
class parent(grandparent):
    def house(self):
        print("100 sqft")
class child(parent):
    def car(self):
        print("BMW")
a=child()
a.land()
a.house()
a.car()'''

#hierarchical-inheritance
class Employee():#parent
    def company(self):
        print("codegnan it soluction")
class Trainer(Employee):#child1
    def teaching(self):
        print("trainer teach the code")
class Developer(Employee):#child2
    def code(self):
        print("developer develops the code")
a=Trainer()
a.teaching()
a.company()
b=Developer()
b.code()
        
        




















