Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#airthematic
a=58
v=88
print(a+v)
146
print(a*v)
5104
print(a-v)
-30
a*=5
print(a)
290
b*=67
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    b*=67
NameError: name 'b' is not defined
b*=57
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    b*=57
NameError: name 'b' is not defined
v*=7
v
616
b=12
b*=57
b
684
t=45
t
45
r=68
r*=45
r
3060
#comparision
a=56
s=47
a,
(56,)
a<s
False
a>S
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a>S
NameError: name 'S' is not defined. Did you mean: 's'?
a>s
True
s<a
True
a==
SyntaxError: invalid syntax
a==s
False
s>=a
False
a<=s
False
#logical
a=45
b=36
a<=b and b>=a
False
a>=b and b>=a
False
a!=b and b<=a
True
>>> not True
False
>>> not False
True
>>> #identify
>>> a=35
>>> type(a)is str
False
>>> type(a)is com
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    type(a)is com
NameError: name 'com' is not defined
>>> type(a) is'com'
False
>>> type(a) is not flot
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    type(a) is not flot
NameError: name 'flot' is not defined. Did you mean: 'float'?
>>> type(a) is not float
True
>>> type(a) is str
False
>>> type(a)is int
True
>>> type(a) is bool
False
>>> type(a)is 'com'
False
>>> type(a) is not complex
True
>>> 
>>> #membership
>>> a=2,56,7,8,9,5
>>> 4 is a
False
>>> 7 is a
False
