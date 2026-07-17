#variable length arguments
'''def check (*a):
    print(a)
    print(type(a))
check()
check(2,3,4,5,6,7,8)
b=[4,5,6,7,8]
check(*b)
c={5,6,7,8,9,10}
check(*c)
d={"name":"sai","age":23,"place":"vja"}
check(*d)'''

'''def check1(*a):
    d=1#creating a variable
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int,float):
            d=d+i
            print(d)
check1()
check1(2,3,4,5,6)
check1(1,3,4,5,2,3,4)
check1(4,3,6,2,3.4,2.3,"python",5+9j,True,False)'''

#**(kwargs)
'''def check2(**a):
    print(a)
    print(type(a))
check2()
details={"names":["sweety","cuty","hearty"],
         "marks":[40,50,70],
         "status":["p","a","p"]}
check2(**details)'''

'''def check2(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)
    
check2()
details={"names":["sweety","cuty","hearty"],
         "marks":[40,50,70],
         "status":["p","a","p"]}
check2(**details)'''

#both * and ** usage
'''def final(*a,**b):
    d=2
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+i
        print(d)
        for i,j in b.items():
            print("key is",i)
            print("value is",j)

final()
data=(2,3,4,5,6,2.3,4.5)
final(*data)
details={"year":[2024,2025,2026],
         "month":["june","july","aug"]}
final(**details)
final(*data,**details)'''


#railway ticket

# Railway Ticket
'''def railway():
    ticket_price = 1000

    while True:
        gender = int(input("""
Select your Gender:
1. Male
2. Female
Enter your choice: """))

        if gender == 1:
            age = int(input("Enter your age: "))
            if age >= 60:
                discount = ticket_price * 30 / 100
            else:
                discount = 0

            total_ticket_price = ticket_price - discount
            print("Ticket Price:", total_ticket_price)

        elif gender == 2:
            age = int(input("Enter your age: "))
            if age >= 60:
                discount = ticket_price * 50 / 100
            else:
                discount = ticket_price * 30 / 100

            total_ticket_price = ticket_price - discount
            print("Ticket Price:", total_ticket_price)

        else:
            print("Invalid choice! Please enter 1 or 2.")

railway()'''






























