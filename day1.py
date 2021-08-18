'''

print('Hello Python')

print("Welcome!!!")
#Single Line comment
print('''A
B
C
D
E''')

'''
Multi Line
Comment
'''






#integer
x=10
y=5
z=x+y
print(z)



#float
x=10.5
y=5.3
z=x+y
print(z)



#Octal
z=0o123
print(z)



#Hexa Decimal
x=0x123AB
print(x)



x=12.4
y=2.7

print(x+y)
print(x-y)
print(x*y)
print(x/y)
#floor division
print(x//y)
#power
print(x**y)
#mod
print(x%y)





a=12
b=8

print('Sum is..',(a+b))


a=12
b=9
c=a>b
print(c)

d=False
print(d)


a='Hello Dear'
b="Welcome!!!!"
c='''This is
multi line string'''

print(a,b,c)





x='Hello'
#immutable
x+'python'
print(x)




a='Hello \n Hi \t Bye'
print(a)






a='This is python code'
print(a[0]) #T
print(a[0:5]) #0-4
print(a[3:]) #3 index onwards

#reverse string
print(a[::-1])

#multi time
print(a*3)

print(len(a))
print(max(a)) #y
print(min(a)) #space


print(a.count('code'))



a='this is My coding Python'
print(a.capitalize())
print(a.title())
print(a.upper())
print(a.lower())
print(a.swapcase())




a='hello'
print(a.islower())
print(a.isupper())
w='a1234'
print(w.isalnum())
r='with'
print(r.isalpha())
d='123'
print(d.isnumeric())
print(a.center(40,'*'))

print(a.find('e')) #1




p='*'
s=["w","t","p","s"]
print(p.join(s))



d='this is is my code'
print(d.split())



s='this \t python \t java'
#tab size change to 20 char
print(s.expandtabs(20))
print(s.startswith('t')) #true
print(s.endswith('t')) #false






a,b,c,d=32,'abc',True,90.3
print(a)
print(b)
print(c)
print(d)
print(type(a))
print(type(b))
print(type(c))
print(type(d))


a='123'
b='54'
print(a+b)
print(int(a)+int(b))



x=89
y=9
print(x+y)
print(str(x)+str(y))




x=12
y=5
z=x+y
print('sum..',z)
del z
#print('sum..',z)







x=[32,54.8,'abc',True,91,False]
print(x)
print(x[2])
print(x[1:4]) #1-3
#no of element
print(len(x))


#update
x[0]=90000
print(x)

#delete
del x[1]
print(x)



x=[[32,54,54],['a','b','c'],[32.54,32,54]]
print(x)



x=[54,12,65,89,90,32]
print(max(x))
print(min(x))
print(len(x))



x=['a','b','p','d','c','m']
#append at end
x.append('test')
print(x)

#insert
x.insert(3, 'xyz')
print(x)




s=['as','ps','as','kr','rr']
#count the elements
print(s.count('as'))
r=['x','y','z']
print(s.extend(r))
print(s)

#1
print(s.index('ps'))

#get last element and remove
print(s.pop())
print(s)

#reverse
s.sort()
s.reverse()
print(s)



s=[90,43,6,1,49,9]
t=sorted(s)
#still same
print(s)
#new list sorted
print(t)


t=sorted(s,reverse=True)
print(s)
print(t)







empdata={'empno':101,
        'name':'Ravi',
        'salary':90000}
print(empdata)
print(empdata['name'])#Ravi
empdata['salary']=130000
print(empdata)
del empdata['name']
print(empdata)


empdata1={'empno':101,
        'name':'Ravi',
        'salary':90000,
        'name':'Anuj'}
print(empdata1)



s={'empno':101,
        'name':'Ravi',
        'salary':78000,
        'city':'pune'}
print(s.keys())
print(s.values())
print(s.get('grade'))

#N/A in place of None
print(s.get('grade','N/A'))


a={'grade':'a','leaves':40}
#after s...a will be appended
s.update(a)
print(s)


a=s.copy()
print(a)




a=['name','city','age']
d=dict.fromkeys(a)
print(d)
r=dict.fromkeys(a,10)
print(r)



#clear
a.clear()
print(a) #blank



s=(21,54,'abc',43.6,True)
#s[1]=3200
#del s[2]


s={32,54,51,54,90}
print(s)



f={'apple','mango','grapes','apple'}
print(f)
f.add('banana')
print(f)
f.remove('mango')
print(f)





import math

print(abs(-90)) #90
print(math.ceil(89.6)) #90
print(math.floor(89.6)) #89
print(math.pow(5,5))
print(math.sqrt(25)) #5
print(max(54,23,654,76))
print(min(54,23,654,76))
print(math.sin(60))
print(math.cos(60))
print(math.tan(60))

print(math.pi)



n=input('Enter your Name please.....')
print('Thanks.....',n)



x=int(input('Enter number.....'))
y=int(input('Enter number.....'))
print(x+y)



x=float(input('Enter number.....'))
y=float(input('Enter number.....'))
print(x+y)



x=float(input('Enter number.....'))

if x>=0:
    print('Positive')
else:
    print('Negative')
    
    
    
    
    



'''x=int(input('Enter number.....'))
y=int(input('Enter number.....'))

if x>y:
    print(x,'is big..')
else:
    print(y,'is big..')
    '''
    


'''Input sale of shop...give discount of 15%
(sale>10000) else discount of 10%. Print final price..

Input   20000
Output  now bill...17000
'''

x=float(input('Enter Sale of shop.....'))
if x>10000:
    dis=x*0.15
else:
    dis=x*0.10
f=x-dis
print(f)



'''Input a name and check it is palindrome or not'''
x=input('Enter Name.....')
if x==x[::-1]:
    print('Palindrome')
else:
    print('Not Palindrome')


x=int(input('Enter number.....'))
s='Valid' if x>10 else 'Invalid'
print(s)

x=int(input('Enter number.....'))
y=int(input('Enter number.....'))
if x>10 and y>10:
    print('Ok')
else:
    print('Not Ok')
    


x=int(input('Enter number.....'))
if x%2==0 or x%5==0:
    print('Valid')
else:
    print('Not Valid')
    
    

    
y=int(input('Enter number.....'))
if not y==10:
    print('Ok')
else:
    print('Not Ok')





s='this is my code'
d=input('Enter letter..')
if d in s:
    print('letter found')
else:
    print('letter not found')
    
    
'''we have a list of cities....input a city from user
and check it is present or not'''



c=['delhi','chennai','pune']
a=input('City....')
if a in c:
    print('Error..')
else:
    c.append(a)
    print(c)
    
 


x=int(input('Enter number'))
if x>0:
    print('+ ve')
elif x<0:
    print('- ve')
else:
    print('zero..')
    
 


c=input('Country..')
if c=='india':
    x=int(input('Age...'))
    if x>=18:
        print('Vote')
    else:
        print('Cannot Vote')
else:
    print('Not Indian')
 
 
 


x=int(input('Number...'))
if x>10:
    pass #null operation
else:
    print('Not Ok')
    
  
    


for i in range(1,11,2):
    print(i)    

for i in range(10,0,-1):
    print(i)   

for i in range(1,11):
    print(i)    

for i in range(11):
    print(i)
else:
    print('end for')


s='my code in python'
for x in s:
    print('letter..',x)


a=['ard','pop','rtt','qww']
for x in a:
    print('Value..',x)





i=1
while i<=10:
    print(i)
    i=i+1
else:
    print('End While')
    






def Hello():
    print('Hi')
    print('Hello')
    print('Ends')
    
print('First')
Hello()
print('Second')
Hello()



#Value pass
#a & b are formal parameters
def calc(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
#calc(90,4)
#calc(40,4)
#calc(30,4)

x=int(input('Enter number'))
y=int(input('Enter number'))
#x & y are actual parameters
calc(x,y)




def fact(x):
    f=1
    while x>=1:
        f=f*x
        x=x-1
    return f
r=int(input('Enter number'))
d=fact(r)
print('Fact...',d)




'''create a fun in which i will pass a list of empno...
it return a dictionary containing all empno
as values with key empno'''



def fun(e):
    d={'empno':e}
    return d
e=[101,102,103,104]
print(fun(e))


def fun(t):
    d={} #blank dictionary
    d['empno']=t
    return d
a=[101,102,103,104]
s=fun(a)
print(s)



def show(empno,name,city):
    print('EmpNo..',empno)
    print('Name..',name)
    print('City..',city)

show(101,'raj','pune')
show(city='delhi',empno=102,name='amit')
show(name='ravi',city='pune',empno=103)



def details(name='test',age=0,salary=0):
    print('Name..',name)
    print('Age..',age)
    print('Salary..',salary)

details('raj',28,89000)
details()
details('amit',29)
details(salary=39000)
details(salary=41000,age=24)



def showdata(*x):
    print('show data')
    for m in x:
        print('Value..',m)
showdata(10)
showdata(32,43)
showdata(32,43,43)
showdata(12,43,43,54)
showdata('ay',43,'xyx',80)


'''create fun that accept n no of value return sum of them'''



def fun(*n):
    s=0
    for m in n:
        s=s+m
    return s

print(fun(10,20,30,40))



#call by reference
def change(d):
    d.append(1000)
r=[21,43,65,675,76]
change(r)
print(r)



def hi():
    global a
    print(a)
    a='Hello'
    print(a)
    
a='My Python'
hi()



#lambda function
Hi=lambda x:x+5
print(Hi(90))



add=lambda a,b:a+b
print(add(10,20))



#Generator function
def basicgen():
    yield 'a'
    yield 'b'
    yield 'c'
x=basicgen()
#print(x)
print(next(x))
print(next(x))
print(next(x))


def basicgenone(x):
    for a in range(x):
        yield a
f=basicgenone(10)
print(next(f))
print(next(f))
print(next(f))



#Comprehensions
x=[12,4,5,7,8,12,14,5,7]
y=[var for var in x if var%2==0]
print(y)



'''


























