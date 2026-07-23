#annonymous function (nameless function)

#calculate function 2*x+5 where x=5
'''def f():
  x=int(input("value"))
  print(2*x+5)
f()'''

#syntax
#a=1ambda arg:expr
'''a=lambda x:2*x+5
print(a(5))'''

'''a=int(input())
b=lambda x:2*x+5
print(b(a))'''

#multiply
'''a=lambda x,y,:x*y
print(a(3,5))'''

'''x=int(input())
y=int(input())
z=lambda x,y,:x*y
print(z(x,y))'''

#CODEGNAN
'''a="codegnan"
b=lambda x:x.upper()
print(b(a))'''

'''a=lambda a:a.upper()
print(a("codegnan"))'''

'''a=lambda a:a.lower()
print(a("SAI"))'''

"python course"
'''a=lambda a:a.title()
print(a("python course"))'''

'''a=lambda a:a.capitalize()
print(a("python course"))'''

#firstname+lastname=fullname
'''fname=input("first name")
lname=input("last name")
fullname=lambda fname,lname:(fname+" "+lname).title()
print(fullname(fname,lname))'''

#using genetrators
'''fname,lname=[x for x in input("enter the name").split(",")]
fullname=lambda fname,lname:(fname+" "+lname).title()
print(fullname(fname,lname))'''
     
#filter()
'''a=[10,30,50,100,127,39,45,67,200]
for i in a:
    if i%2==0:
        print(i)'''

'''b=list(filter(lambda x:x%2==0,a))
print(b)'''

#[],(),{}
'''a=[]
print(type(a))

b=()
print(type(b))

c={}
print(type(c))'''

#printing non-empty value in the list
'''a=[[],(),set(),{}," ",None,5,8,9,"python",5+9j,True,False]
b=list(filter(None,a))
print(b)'''








    
















