#generations
#[expr for var in collection/range]
'''a=[i for i in range(16)]
print(a)
print(type(a))'''

#(expr for var in collection/range)
'''a=(i for i in range(16))
print(a)
print(*a)
print(type(a))

b=list(a)
print(a)

#print(tuple(a))
print(set(a))'''

#generators
'''a,b=[int(x) for x in input("enter the values")
.split(",")]
def check(a,b):
    while a<b:
        #yield a
        a-a+1
        yield a
print(*check(a,b))'''

'''a,b=[int(x) for x in input("enter the values").split(",")]
def check(a,b):
    while a<b:
        a=a+1
        #return a
    return a
print(check(a,b))'''

#yield v/s return
'''def mygen():
    #return "vja"
    #return "hyd"
    #return "vzg"
    #return "vja","hyd","vzg"
print(*mygen())'''

'''def mygen():
    yield "python"
    yield "java"
    yield "DSA"
print(*mygen())

#next()
d=mygen()
print(next(d))
print(next(d))
print(next(d))'''





























          






