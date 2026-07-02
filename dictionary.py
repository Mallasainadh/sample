Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a={"college":"urcle","branch":"cse"}
a.get("college")
'urcle'
a["branch"]
'cse'
a
{'college': 'urcle', 'branch': 'cse'}
a={"hour":12,"min":3,"sec":60}
a.copy()
{'hour': 12, 'min': 3, 'sec': 60}
a
{'hour': 12, 'min': 3, 'sec': 60}
a.clear()
a
{}
b={}
b.update({"name":"sai"})
b
{'name': 'sai'}
b.clear()
b
{}
b
{}
a={"name":"sai":"course":"python":"city":"vja"}
SyntaxError: invalid syntax
a={"name":"sai","course":"python","city":"vja"}
print(a)
{'name': 'sai', 'course': 'python', 'city': 'vja'}
a={"namel":"pooja","city":"vja","name2":"sai"}
print(a)
{'namel': 'pooja', 'city': 'vja', 'name2': 'sai'}
a={"idnos
   
SyntaxError: unterminated string literal (detected at line 1)
'a="idnos":[10,20,30,40,50],"names":["sai","kumar",karthik"],"marks":[60,70,80,90]}
   
SyntaxError: unterminated string literal (detected at line 1)
a="idnos":[10,20,30,40,50],"names":["sai","kumar",karthik"],"marks":[60,70,80,90]}
                                    
SyntaxError: unterminated string literal (detected at line 1)
a="idnos":[10,40,50],"names":["sai","kumar","karthik"],"marks":[60,70,50]}
   
SyntaxError: unmatched '}'
{a="idnos":[10,20,50],"names":["sai","kumar","karthik"],"marks":[70,80,90]}
   
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a={"idnos":[10,20,50],"names":["sai","kumar","karthik"],"marks":[70,80,90]}
   
a
   
{'idnos': [10, 20, 50], 'names': ['sai', 'kumar', 'karthik'], 'marks': [70, 80, 90]}
a=[9,1,5,2,8,4,6,3,7,0]
   
#[7,6,4,3,0,9,8,5,2,1]
   
a1=[o:5
    
SyntaxError: invalid syntax
a1={0:5]
    
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
>>> 
>>> a1=[0:5]
...     
SyntaxError: invalid syntax
>>> a1=[0:5]
...     
SyntaxError: invalid syntax
>>> a1=a[0:5]
...     
>>> a1
...     
[9, 1, 5, 2, 8]
>>> a1.sort()
...     
>>> a1
...     
[1, 2, 5, 8, 9]
>>> a2.sort()
...     
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    a2.sort()
NameError: name 'a2' is not defined. Did you mean: 'a'?
>>> a2=a[5:10]
...     
>>> a2
...     
[4, 6, 3, 7, 0]
>>> a2.sort()
...     
>>> a2
...     
[0, 3, 4, 6, 7]
>>> a1.reverse()
...     
>>> a1
...     
[9, 8, 5, 2, 1]
