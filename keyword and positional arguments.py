#keyword and positional arguments
'''def details(id,name,mailid):
    id=20
    name="sai"
    mailid="sai1432gmail.com"
    print(id,name,mailid)
details(id="id",name="name",mailid="mailid")'''

'''def details(id,name,mailid):
    print(id,name,mailid)
details(id="id",name="name",mailid="mailid")
details(id=20,name="sai",mailid="sai1432gmail.com")
details(id=30,name="karthik",mailid="karthik@gmail.com")
details(40,"ganesh","ganesh@gmail.com")
details("chinni@gmail.com",60,"chinni")
details(mailid="srinu@gmail.com",id=70,name="srinu")'''

#defaulat arguments
'''def grocery(item="rice",price=1500):
    print("item is %s" %item)
    print("price is %.2f" % price)
grocery()'''

'''def grocery(item,price=200):
    print("item is %s" %item)
    print("price is %.2f" % price)
grocery("dhal")'''

'''def grocery(item="ghee",price):
    #non def arg follows def arg
    print("item is %s" %item)
    print("price is %.2f" %item)
grocery(500)'''


'''def bakery(cake_name,price,qty):
    print("cake is %s" %cake_name)
    print("price is %.2f" %price)
    print("quantity is %d." %qty)
bakery("staberry",500,1)'''

#* arguments (*is used to unpack the elements)
'''a=[2,3,4,5,6,7]
print(a)
print(*a)'''

'''a=[2,3,4,5,6,7]
print(a)
print(*a)'''

'''a=[2,3,4,5,6,7]
print(a)
print(*a)'''

'''b={"name":"sai","city":"vja"}
print(b)
print(*b)'''

'''a,b,c=2,3,4,5,6,7,8,9,10
print(a)
print(b)
print(c)'''  #error

'''a,b,c="cod"
print(a)
print(b)
print(c)'''

a,b,*c="codegnan"
print(a)
print(b)
print(*c)



















