'''
import sys
print('Hi Dear...')
print(sys.argv[1])
print('File..',sys.argv[0])




import sys
print('No of values....')
print(len(sys.argv))




import sys
a=int(sys.argv[1])
b=int(sys.argv[3])
c=sys.argv[2]
if c=='+':
    print(a+b)
if c=='-':
    print(a-b)
if c=='*':
    print(a*b)
if c=='/':
    print(a/b)



a=int(input('Enter number...'))

b=int(input('Enter number...'))

c=a/b

print('Answer...',c)




try:
    a=int(input('Enter number...'))
    b=int(input('Enter number...'))
    c=a/b
    print('Answer...',c)

except ZeroDivisionError:
    print('Check 2nd number...')




Replicate multiple exception scenario in single code. 
example command line values...
exception...IndexError ValueError ZeroDivisionError

python First.py 12 3
python First.py (index error)
python First.py a b (value error)
python First.py 12 0 (division error)



import sys
try:
    a=int(sys.argv[1])
    b=int(sys.argv[2])
    c=a/b
    print('Answer...',c)

except IndexError:
    print('Please enter value....')
    
except ValueError:
    print('Enter correct value')

except ZeroDivisionError:
    print('Check 2nd number...')





try:
    a=int(input('Enter number...'))
    b=int(input('Enter number...'))
    c=a/b
    print('Answer...',c)

except Exception as ex:
    print('Any issue...',ex)




try:
    a=int(input('Enter number...'))
    b=int(input('Enter number...'))
    c=a/b
    print('Answer...',c)

except:
    print('Any issue...')





try:
    a=int(input('Enter number...'))
    b=int(input('Enter number...'))
    c=a/b
    print('Answer...',c)

except:
    print('Any issue...')
    
finally:
    print('The Ends....')





try:
    a=int(input('Enter number...'))
    if a<10:
        raise Exception()
    else:
        print('Ok...')

except:
    print('Any issue...')
    
finally:
    print('The Ends....')





class MyException(Exception):
    def showmessage(self):
        print('My Issue')
try:
    a=int(input('Enter number...'))
    if a<10:
        raise MyException()
    else:
        print('Ok...')
except MyException as ex:
    ex.showmessage()

    


a=int(input('Enter number...'))
assert a<10


a=int(input('Enter number...'))
assert a<10,"Check this"


'''





