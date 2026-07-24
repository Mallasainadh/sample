#max(),min(),sum()
'''print(max(4,5,7,8,10,20))

#min()
print(min(2,3,4,5,6,7))

#sum()
a=3,4,5,6,7,8,9,10,11
print(sum(a))'''

#map
'''a=[2,5,7,8,10,12,14,16,20,25]
b=[1,3,5,7,9,11,15,17,21,24,30]
c=list(map(max,a,b))
print(c)
c=list(map(min,a,b))
print(c)'''

'''a=input("datal")
b=input("data2")
print(a+b)'''

'''a,b=input("enter the names").split(",")
print(a+b)'''

'''a,b=[x for x in input("names").split(",")]
print(a+b)'''

'''a,b=map(str,input("enter the names").split(","))
print(a+b)'''

'''a=int(input())
b=int(input())
print(a+b)'''

'''a,b=[int(x) for x in input().split(",")]
print(a+b)'''

'''a,b=[int(input()).split(",")
print(a+b)#error'''

'''a,b=map(int,input("enter the values").split(","))
print(a+b)'''

'''a,b=list(map(int,input("enter the values").split(","))
print(a)
print(type(a))'''

'''a,b=tuple(map(int,input("enter the values").split(",")))
print(a)
print(type(a))'''

'''a,b=set(map(int,input("enter the values").split(",")))
print(a)
print(type(a))'''

'''a,b=list(map(int,input("enter the values").split(",")))
print(a)
print(type(a))'''

'''a,b=list(map(eval,input("enter the values").split(",")))
print(a)
print(type(a))'''


'''a=input("enter the key and value pairs")
b=dict(i.split(":") for i in a.split(","))
print(b)'''

#marks -analysis report
'''students=int(input("no of students"))
marks=[]
for i in range(1,students+1):
    mark=int(input(f"enter the student{i} marks"))
    marks.append(mark)
for i in marks:
    print(i)
print("...........marks analaysis report..........")
print("total no.of students",students)
print("heighest marks",max(marks))
print("lowest marks",sum(marks))
print("total marks",sum(marks))
print("average",sum(marks)/students)'''




















