Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #string method
>>> a="python"
>>> len(a)
6
>>> b="python course"
>>> len(b)
13
>>> c=""
>>> len(c)
0
>>> d=" "
>>> len(d))
SyntaxError: unmatched ')'
>>> a="twinkle twinkle little star"
>>> count(a)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
>>> a.count("twinkle")
2
>>> a.count("t")
5
>>> #find string
>>> a="code"
>>> a[1]
'o'
>>> a.find("d")
2
>>> a.find("e")
3
>>> b="hello"
>>> b.find("1")
-1
>>> b[2:4]
'll'
>>> #escape sequences
>>> a="name\nmobile\tmailid\nclg"
print(a)
name
mobile	mailid
clg
#replace()
a="wait until you succeed"
a.replce ("wait","work")
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    a.replce ("wait","work")
AttributeError: 'str' object has no attribute 'replce'. Did you mean: 'replace'?
a.replace("wait","work")
'work until you succeed'
a
'wait until you succeed'
b="wait until you succeed"
b.replace ("wait","work")
'work until you succeed'
b
'wait until you succeed'
#upper()
a="hello"
a.upper()
'HELLO'
#lower()
b="HI"
b.lower()
'hi'
c="python"
c.upper()
'PYTHON'
c.capitalize()
'Python'
a="python course"
a.title()
'Python Course'
a="java"
a.isupper()
False
a.islower()
True
a.isdight()
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    a.isdight()
AttributeError: 'str' object has no attribute 'isdight'. Did you mean: 'isdigit'?
a.'isdigit'()
SyntaxError: invalid syntax
a.isdigit ()
False
a.isalpha ()
True
b="python course"
b.isalpha()
False
c="python course"

c.isalpha ()
False
d="1234"
d.isdigit ()
True
d.isalnum ()
True
e="pooja 1234"
e.isalnum ()
False
f="pooja@1234"
f.isalnum ()
False
a="hello python"
a.startswith("h")
True
a.endwith ("n")
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    a.endwith ("n")
AttributeError: 'str' object has no attribute 'endwith'. Did you mean: 'endswith'?
a.endswith ("n")
True
#strip()
lstrip(),rstrip()
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    lstrip(),rstrip()
NameError: name 'lstrip' is not defined
a="
SyntaxError: unterminated string literal (detected at line 1)
a="  pooja
SyntaxError: unterminated string literal (detected at line 1)
l strip (),r strip ()
SyntaxError: invalid syntax
l strip (),r strip ()
SyntaxError: invalid syntax
lstrip(), rstrip()
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    lstrip(), rstrip()
NameError: name 'lstrip' is not defined
a.lstrip()
'hello python'
a.rstrip()
'hello python'
#split
a="python java c c++
SyntaxError: unterminated string literal (detected at line 1)
a="python java c c++"
a.split ()
['python', 'java', 'c', 'c++']
b="iam in vja"
b.split ()
['iam', 'in', 'vja']
c="codegnan"
c.split ()
['codegnan']
#join
a="vja hyd vzg"
",join(a)
SyntaxError: unterminated string literal (detected at line 1)
'join (a)
SyntaxError: unterminated string literal (detected at line 1)
" ,join (a)
SyntaxError: unterminated string literal (detected at line 1)
print(""join(a))
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print("",join(a) )
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    print("",join(a) )
NameError: name 'join' is not defined
".join(a)
SyntaxError: unterminated string literal (detected at line 1)
"".join(a)
'vja hyd vzg'
b="vja","hyd","vzg"
"".join(b)
'vjahydvzg'
"k".join (b)
'vjakhydkvzg'
a="hello"
b="world"
print(a+b)
helloworld
print(a+" "+b)
hello world
fname="pooja"
lname="ch"
print(fname+lname)
poojach
print(fname+" "+lname)
pooja ch
print(fname.title()+" "+lname.title() )
Pooja Ch
print(fname+" "+lname).title() )
SyntaxError: unmatched ')'
print (fname+" "+lname).title())
SyntaxError: unmatched ')'
print (fname+" "+lname).title()
pooja ch
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    print (fname+" "+lname).title()
AttributeError: 'NoneType' object has no attribute 'title'
#formatting
a=4
b=8
print (a+b)
12
print("the sum is ",a+b)
the sum is  12
x="vja"
print("city is ",x)
city is  vja
#format method
a="motu
SyntaxError: unterminated string literal (detected at line 1)
a+"motu"
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    a+"motu"
TypeError: unsupported operand type(s) for +: 'int' and 'str'
a="motu"
b="patlu"
print ("hello",a+b)
hello motupatlu
print("hello{} {}",format (a,b))
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    print("hello{} {}",format (a,b))
ValueError: Invalid format specifier 'patlu' for object of type 'str'
print ("hello{}{}".format (a,b))
hellomotupatlu
#fstring
a="sita"
b="ram"
print (f"hello {a} {b}")
hello sita ram
print (f"hello {a}{b}")
hello sitaram
print (f"hello {a}hello{b}")
hello sitahelloram
a=4
b=5
c=a*b
print("the product is {}"format (c)
      
SyntaxError: '(' was never closed
print("the product is {}"format (c))
      
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print(" the product is {}"format (c))
      
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print(". the product is {}"format (c))
      
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print("the product is {}".format(c))
      
the product is 20
print
      
<built-in function print>9
print(f"the product is {c}")
      
the product is 20
print("the product is {}".format (a*b))
      
the product is 20
print(f"the product is {a*b}")
      
the product is 20
