'''
import mymodule

mymodule.sum(3, 2)
mymodule.hello()
print(mymodule.square(40))



from mymodule import sum,square
sum(8, 2)
print(square(8))



from mymodule import *
sum(7,2)
print(square(4))
hello()




import mymodule as mp
mp.sum(8, 3)
print(mp.square(7))
mp.hello()





import time
t=time.time()
#no of tiks
print(t)
#complete date/time info
d=time.localtime(t)
print(d)
#format date/time
r=time.asctime(d)
print(r)






import calendar
c=calendar.month(2021, 8)
print(c)




import datetime
d=datetime.datetime.now()
print(d)





import datetime
d=datetime.datetime.now()
print(d)
print(d.year)
print(d.month)
print(d.date())
print(d.hour)
print(d.minute)
print(d.second)





class Employee:
    empno=0
    name=''
obj=Employee()
obj.empno=101
obj.name='Rajeev'
print(obj.empno)
print(obj.name)




class Employee:
    empno=0
    name=''
    def get(self,a,b):
        self.empno=a
        self.name=b
    def show(self):
        print(self.empno)
        print(self.name)
obj=Employee()
obj.get(101,'Raj')
obj.show()
obj1=Employee()
obj1.get(102,'Amit')
obj1.show()





class Employee:
    empno=0
    salary=0
    grade=''
    def get(self,a,b):
        self.empno=a
        self.salary=b
    def check(self):
        if self.salary>=30000:
            self.grade='A'
        else:
            self.grade='B'
    def show(self):
        self.check()
        print(self.empno)
        print(self.salary)
        print(self.grade)
obj=Employee()
obj.get(103,31000)
obj.show()




class Employee:
    empno=101
    salary=21000
    grade='A'
obj=Employee()
print(hasattr(obj, 'empno')) #true
print(getattr(obj, 'salary'))
setattr(obj, 'salary',45000)
print(getattr(obj, 'salary'))
delattr(obj, 'empno')
print(hasattr(obj, 'empno')) #error





class Employee:
    empno=0
    salary=0
    grade=''
    
    def __init__(self):
        self.empno=101
        self.salary=34000
        self.grade='A'
        print('Const. called')
        
    def show(self):
        print(self.empno)
        print(self.salary)
        print(self.grade)

obj=Employee() #__init__ calls
obj.show()



class Employee:
    empno=0
    salary=0
    grade=''
    #parameteriezed
    def __init__(self,a,b,c):
        self.empno=a
        self.salary=b
        self.grade=c
        print('Const. called')
        
    def show(self):
        print(self.empno)
        print(self.salary)
        print(self.grade)

obj=Employee(101,43000,'B') #__init__ calls
obj.show()





class Employee:
    empno=0
    salary=0
    grade=''
    
    def __init__(self,a,b,c):
        self.empno=a
        self.salary=b
        self.grade=c
        print('Const. called')
        
    def show(self):
        print(self.empno)
        print(self.salary)
        print(self.grade)
        
    def __del__(self):
        print('Bye...')

obj=Employee(101,43000,'B') #__init__ calls
obj.show()
obj1=Employee(102,41000,'A')
obj1.show()




#Inheritance
class A:
    def hello(self):
        print('Hello')
        print('Parent')
#B is child of A
class B(A):
    def sum(self,a,b):
        print('Sum..',(a+b))
        
obj=B()
obj.sum(32, 54)
obj.hello()




class A:
    def hello(self):
        print('Hello')
        print('Parent')
#B is child of A
class B(A):
    def sum(self,a,b):
        print('Sum..',(a+b))
#C is child of B
class C(B):
    def Hi(self):
        print('Hi C....')
        
obj=C()
obj.hello()
obj.Hi()
obj.sum(12, 3)





class A:
    def hello(self):
        print('Hello')
        print('Parent')
class B:
    def sum(self,a,b):
        print('Sum..',(a+b))
#C is child of A and B
class C(A,B):
    def Hi(self):
        print('Hi C....')
        
obj=C()
obj.hello()
obj.Hi()
obj.sum(12, 3)



class A:
    def hello(self):
        print('hello')
        print('parent')
    def __str__(self):
        return "My A class..."
obj=A()
print(obj)




class A:
    #hidden
    __name='Rajeev'
obj=A()
print(obj.__name)

'''











