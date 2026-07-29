#exception handling
'''while True:
    try:
        a=int(input("a value"))
        b=int(input("b value"))
        c=a//b
        print(c)
    except:
        print("exception is raised")
    else:
        print("no exceptions")
    finally:
        print("program ends.....")'''

#regex(regular expressions)
a="codegnan is in vijayawada"
print(a)

a="codegnan\nis\tin\nvijayawada"
print(a)

#rstring
a=r"codegnan\nis\tin\nvja"
print(a)

#compile(),search(),findall(),split(),sub()

#sequence characters
'''\w->it matches alphanumeric
\w->it matches non-alpha numeric
\d->it matches any digit
\D->it matches non-digit
\s->it represents white spaces
\s->it represent non-white spaces'''

#compile()
import re
a="mat cat cap maths money cash code cup dog donkey mu"
'''b=re.compile(r"m\w\w\w\w")
print(b)'''

#search()
'''c=b.search(a)
print(c)'''

'''b=re.search(r"m\w+",a)
print(b)'''

#findall()
'''c=re.findall(r"c\w+",a)
print(c)'''

#split()
'''d=re.split(r"w",a)
print(d)'''

'''e=re.spilt(r"\s",a)
print(e)'''

#sub()
'''f=re.sub("m","a",a)
print(f)'''

'''e="code dog donkey"
f=re.findall(r"d\w+",e)
print(f)'''




































