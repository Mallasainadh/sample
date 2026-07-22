#built-in functions
#print(dir())

#print(dir("_builting_"))

#from keys()
'''a="codegnan"
print(a)
print(list(a))
print(tuple(a))

print(set(a))
#print(dict(a))
b=dict.fromkeys(a)
print(b)

c=dict.fromkeys(a,"sai")
print(c)

c["d"]="python"
print(c)'''

#evaluate()
'''while True:
    a=int(input("a value))
    b=int(input("b value))
    print(a+b)'''            
                
'''while True:
    a=input("a value")
    b=input("b value")
    print(a+b)'''

'''while True:
    a=eval(input("a value"))
    b=eval(input("b value"))
    print(a+b)'''

#zip()->we can combine multiple collections into one collection
a=[10,20,30,40,50,60]
names=["sai","manoj","karthik","teja"]
'''b=zip(a,names)
print(b)'''

c=list(zip(a,names))
print(c)

c=tuple(zip(a,names))
print(c)

c=set(zip(a,names))
print(c)

c=dict(zip(a,names))
print(c)

#enumerate()=>we can give counter to the collection
names=["srinu","surya","aakesh","venkatesh","babu"]
'''for i in range(len(names)):
    print(i,names[i])'''

'''b=list(enumerate(names))
print(b)

b=list(enumerate(names,20))
print(b)

b=dict(enumerate(names,100))
print(b)'''

#ASCII
#chr()
#ord()
print(chr(67))

print(chr(58))

print(chr(95))

print(ord("f"))

print(ord("z"))

#print(chr("g")) error

'''for i in range(65,91):
    print(chr(i),end=" ")

for i in range(97,123):
    print(chr(i),end=" ")'''

'''a=input("enter your name")
for i in a:
    print(i,"_",ord(i))'''

#BMI
while True:
    weight=eval(input("Enter your weight:"))
    height=eval(input("Enter your height:"))
    BMI=(weight/height**2)
    print(f"Your BMI is {BMI}")
    if BMI<=18.5:
        print("Under Weight")
    elif 18.5<=BMI<=24.5:
        print("Healthy Weight")
    elif 24.5<=BMI<=29.5:
        print("Over Weight")
    elif BMI>=30:
        print("Obesity")
























