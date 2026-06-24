Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=20
print(a)
20
a+b=30
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
a=10
b=30
print(a+b)
40
a=c=20
print(a,c)
20 20
a,b,c,d
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a,b,c,d
NameError: name 'd' is not defined. Did you mean: 'id'?
>>> a,b,c=4+5+9
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a,b,c=4+5+9
TypeError: cannot unpack non-iterable int object
>>> a,b,c=2,5,6
>>> print(a,b,c)
2 5 6
>>> a=60
>>> b=70
>>> print(b*a)
4200
>>> firstname=sainadh
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    firstname=sainadh
NameError: name 'sainadh' is not defined
>>> firstname=''sainadh''
SyntaxError: invalid syntax. Is this intended to be part of the string?
>>> first_name="sainadh"
>>> print(firstname)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print(firstname)
NameError: name 'firstname' is not defined. Did you mean: 'first_name'?
>>> print(first_name)
sainadh
>>> fname="sainadh"
>>> lname="malla"
>>> print(fname+lname)
sainadhmalla
>>> print(fname+''+lname)
sainadhmalla
>>> name="sainadh"
>>> print(name)
sainadh
>>> print(NAME)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print(NAME)
NameError: name 'NAME' is not defined
>>> PRINT(NAME)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    PRINT(NAME)
NameError: name 'PRINT' is not defined
