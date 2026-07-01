Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list[]
a=[2,5.6,"python",6+9j,True,False]
print(a)
[2, 5.6, 'python', (6+9j), True, False]
type(a)
<class 'list'>
b=5
type(b)
<class 'int'>
c=5
type(c)
<class 'int'>
#append()
a.append(["ml","ai"])
a
[2, 5.6, 'python', (6+9j), True, False, ['ml', 'ai']]
#extent()
a=["ml","ai","ds"]
a.extend(["c","c++","python"])
a
['ml', 'ai', 'ds', 'c', 'c++', 'python']
#insert()
b.insert(l,"vzg")
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    b.insert(l,"vzg")
AttributeError: 'int' object has no attribute 'insert'
b=["vja","hyd"]
b.insert(l,"vzg")
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    b.insert(l,"vzg")
NameError: name 'l' is not defined
b.insert(1,"vzg")
b
['vja', 'vzg', 'hyd']
#copy()
a=["black","white","pink","red"]
a.index("white")
1
a.copy()
['black', 'white', 'pink', 'red']
b=a.copy()
b
['black', 'white', 'pink', 'red']
b.count("pink")
1
#sort()
a=["grapes","apples","mango","banana"]
a.sort()
a
['apples', 'banana', 'grapes', 'mango']
b=[8,6,0,3,2,5,1]
b.sort()
b
[0, 1, 2, 3, 5, 6, 8]
#reverse()
a=[7,8,9,10.12,13,14,15]
a.reverse()
a
[15, 14, 13, 10.12, 9, 8, 7]
b=[10,20,29,48,56,67,48]
b.reverse()
b
[48, 67, 56, 48, 29, 20, 10]
b=["java","html","css"]
b.reverse()
b
['css', 'html', 'java']
#pop()
a=["c","c++","ml","ai"]
a.pop()
'ai'
a
['c', 'c++', 'ml']
>>> a.pop(1)
'c++'
>>> a
['c', 'ml']
>>> #REMOVE()
>>> a.REMOVE("C")
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    a.REMOVE("C")
AttributeError: 'list' object has no attribute 'REMOVE'
>>> a.remove("c")
>>> a
['ml']
>>> #examples
>>> a=["pooja","priya","prince","sweety"]
>>> len(a)
4
>>> b="pooja"
>>> len(b)
5
>>> c="pooja"
>>> len9c0
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    len9c0
NameError: name 'len9c0' is not defined
>>> len(c)
5
>>> #clear
>>> a.clear()
>>> a
[]
>>> b=[]
>>> b.append
<built-in method append of list object at 0x00000199B6153740>
>>> b.append("hi")
>>> b
['hi']
