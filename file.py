'''
empno='E0001'
name='Amit'
city='Delhi'

obj=open('Data.txt','w')

obj.write(empno+'\n')
obj.write(name+'\n')
obj.write(city+'\n')

print('Data Saved....')

obj.close()





empno=int(input('Enter Empno....'))
name=input('Enter Name....')
city=input('Enter City....')

fn=input('Enter FileName....')
#append mode
obj=open(fn,'a')

obj.write(str(empno)+'\n')
obj.write(name+'\n')
obj.write(city+'\n')

print('Data Saved....')

obj.close()






x=input('Enter file to read')
f=open(x,'r')
#no of letters to read
st=f.read(200)
print(st)
f.close()



import datetime
d=datetime.datetime.now()

if d.day==1:
    x=input('Enter file to read')
    f=open(x,'r')
    st=f.read(200)

    y=input('Enter file to write')
    f=open(y,'w')
    f.write(st)

f.close()




x=input('Enter file to read')
f=open(x,'r')
l=0
u=0
s=f.read()
for i in range(len(s)):
    if(s[i]>='a' and s[i]<='z'):
        l+=1
    elif(s[i]>='A' and s[i]<='Z'):
        u+=1
print('lower letters=',l)
print('upper letters=',u)




x=input('Enter file to read')
f=open(x,'r')
st=f.read(600)
l=0
u=0
d=0
s=0
for r in st:
    if r.isdigit():
        d+=1
    if r.isupper():
        u+=1
    if r.islower():
        l+=1
    if r.isspace():
        s+=1
print('Digits..',d)
print('Upper..',u)
print('Lower..',l)
print('Space..',s)
f.close()





f=open('EmpData.txt','r')
st=f.read(600)

print(st)

pos=f.tell()
print('Position..',pos)
f.close()




f=open('EmpData.txt','r')

st=f.read(150)
print(st)
pos=f.tell()
print('Position..',pos)
pos=f.seek(0,0)
st=f.read(10)
print(st)
f.close()




f=open('EmpData.txt','r')

print(f.closed)
print(f.mode)
print(f.name)
f.close()

'''









