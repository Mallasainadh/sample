Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#tuple()
a=(4,5.6,"code",5+9j,True,False)
print(a)
(4, 5.6, 'code', (5+9j), True, False)
type(a)
<class 'tuple'>
a.count(5+7j)
0
a.index(True)
4
a.index(False)
5
len(a)
6
#sets{}
a={5,6,3.5,"sai",5+7j,True,False)
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
a={5,6,3.5,"sai",5+7j,True,False}
print(a)
{False, True, 3.5, 5, 6, 'sai', (5+7j)}
type(a)
<class 'set'>
a={3,5,4,6,78}
b={1,5,7,9,45}
b.issubset(a)
False
a.issubset
<built-in method issubset of set object at 0x000002CDBE489D20>
9
a.issubset(b)
False
a.issupersubset(b)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a.issupersubset(b)
AttributeError: 'set' object has no attribute 'issupersubset'. Did you mean: 'issuperset'?
a.issuperset(b)
False
b.issupperset(a)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    b.issupperset(a)
AttributeError: 'set' object has no attribute 'issupperset'. Did you mean: 'issuperset'?
b.issuperset(a)
False
#union
a={2,4,6,8,75,3,7}
b={1,2,3,4,5,6,7}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 75}
c={1,45,37,46,39,}
print(c)
{1, 37, 39, 45, 46}
#intersection()
a={3,4,5,6,7,8,9}
b={2,3,5,6,78,8,9}
a.intersection(b)
{3, 5, 6, 8, 9}
#update()
a={10,20,30,40,50}
b={50,60,70,80,90}
a
{50, 20, 40, 10, 30}
a.update(b)
a
{70, 40, 10, 80, 50, 20, 90, 60, 30}
b
{80, 50, 70, 90, 60}
b.update(a)
b
{70, 40, 10, 80, 50, 20, 90, 60, 30}
#defference
a={36,55,46,78,59,38}
b={78,56,59,38,37,68}
a.difference(b)
{36, 46, 55}
b.difference(a)
{56, 68, 37}
#symmetric difference
a={3,4,5,6,7,8,,9}
SyntaxError: invalid syntax
a={3,4,5,6,7,8,9}
b={1,4,2,7,8,9,10}
a.symmetric_difference(b)
{1, 2, 3, 5, 6, 10}
#intersection_update(b)
a={1,2,4,3,5,7,8,99}
b={2,4,6,9,55,12,45}
a.intersection_update(b)
a
{2, 4}
b.intersection_update(a)
b
{2, 4}
#difference_update
a={2,3,4,5,6,7}
b={9,8,7,56,4,2}
a.difference_update(b)
a
{3, 5, 6}
b.difference_update(a)
b
{2, 4, 7, 8, 9, 56}
#symmetric_difference_update
a={11,12,13,14,15,16,17}
b={14,13,15,16,17,18,19}
a.symmeric_difference_update
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    a.symmeric_difference_update
AttributeError: 'set' object has no attribute 'symmeric_difference_update'. Did you mean: 'symmetric_difference_update'?
9
a.symmeric_difference_update(b)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    a.symmeric_difference_update(b)
AttributeError: 'set' object has no attribute 'symmeric_difference_update'. Did you mean: 'symmetric_difference_update'?
>>> a.symmetric_difference_update(b)
>>> a
{11, 12, 18, 19}

>>> #pop()
>>> a={4,5,6,7,8}
>>> a.pop()
4
>>> a.remove(7)
>>> a
{5, 6, 8}
>>> #discard
>>> #discard()
>>> a={3,4,5,6,7,8}
>>> a.discard(7)
>>> a
{3, 4, 5, 6, 8}
>>> a.clear()
>>> a
set()
>>> b=set()
>>> b.add(30)
>>> b
{30}
>>> #count()
>>> a={3,4,5,6,7}
>>> len(a)
5
>>> #disjoint
>>> a=1,2,3,4,5,6}
SyntaxError: unmatched '}'
>>> a={1,2,3,4,5,6}
>>> b={6,7,8,9,34,5}
>>> a.isdisjoint(b)
False
>>> b.isdisjoint(a)
False
