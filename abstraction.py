Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#abstraction
'''class A():
    def method1(self):
        pass
obj1=A()
obj.method1()'''

'''class A():
    def method1(self):
        print("python")
obj1=A()
... obj1.method1()'''
... 
... '''from abc import ABC,abstractmethod
... class A():
...     def method1(self):
...         print("data")
... obj1=A()
... obj1.method()'''
... 
... '''from abc import ABC,abstractmethod
... class A(ABC):
...     @abstractmethod
...     def method1(self):
...         print("codegnan")
... obj1=A()
... obj1.method1()'''
... 
... '''from abc import ABC,abstractmethod
... class A(ABC):
...     @abstractmethod
...     def method1(self):
...         pass
...     def method2(self):
...         print("python course")
...     @abstractmethod
...     def method3(self):
...         pass
... class B(A):
...     def method1(self):
...         print("data science")
...     def method3(self):
...         print("machine learning")
... obj1=B()
... obj1.method1()
... obj1.method2()
... obj1.method3()'''
... 
... 
... 
