Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #dict()
>>> a={"name":"rajesh","city":"vja"}
>>> print(a)
{'name': 'rajesh', 'city': 'vja'}
>>> type(a)
<class 'dict'>
>>> b={2,4,6,7,9,"city"}
>>> type(b)
<class 'set'>
>>> a={"name":"sai","mailid":"sainadh@469","mobileno":9396239917}
>>> print(a)
{'name': 'sai', 'mailid': 'sainadh@469', 'mobileno': 9396239917}
>>> a.key()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a.key()
AttributeError: 'dict' object has no attribute 'key'. Did you mean: 'keys'?
>>> a.keys()
dict_keys(['name', 'mailid', 'mobileno'])
>>> a.values()
dict_values(['sai', 'sainadh@469', 9396239917])
>>> a.items()
dict_items([('name', 'sai'), ('mailid', 'sainadh@469'), ('mobileno', 9396239917)])
>>> #update
>>> a={"course":"python","mentor":"pooja"}
>>> a.update({"student":"rajesh"})
>>> print(a)
{'course': 'python', 'mentor': 'pooja', 'student': 'rajesh'}
>>> b={"year":2026,"month":"july"}
>>> b.setdefault("date",2)
2
>>> print(b)
{'year': 2026, 'month': 'july', 'date': 2}
>>> a={"time":10,"hour":2,"min"23}
SyntaxError: ':' expected after dictionary key
>>> a={"time":10,"hour":2,"min":23}
>>> a.pop("hour")
2
print(a)
{'time': 10, 'min': 23}
