'''
import pymysql
#step 1
d=pymysql.connect(host='localhost',user='root',password='Cloud@123$',db='fis')
#step 2
cur=d.cursor()
sql="select version()"
#step 3
cur.execute(sql)
data=cur.fetchone()
print(data)
d.close()




import pymysql

d=pymysql.connect(host='localhost',user='root',password='Cloud@123$',db='fis')

cur=d.cursor()
sql="select * from employee"

cur.execute(sql)
data=cur.fetchall()
for res in data:
    print('Empno..',res[0])
    print('Name..',res[1])
    print('City..',res[2])
    print('Salary..',res[3])
d.close()





import pymysql
try:
    d=pymysql.connect(host='localhost',user='root',password='Cloud@123$',db='fis')

    cur=d.cursor()
    sql="insert into employee values(106,'Ravi','Pune',31000)"

    cur.execute(sql)
    d.commit()
    print('Data Inserted..')
except Exception as ex:
    print(ex)
d.close()




import pymysql
try:
    d=pymysql.connect(host='localhost',user='root',password='Cloud@123$',db='fis')

    cur=d.cursor()
    sql="delete from employee where empno=101"

    cur.execute(sql)
    d.commit()
    print('Data Deleted..')
except Exception as ex:
    print(ex)
d.close()





import pymysql
try:
    d=pymysql.connect(host='localhost',user='root',password='Cloud@123$',db='fis')

    cur=d.cursor()
    sql="update employee set salary=70000 where empno=102"

    cur.execute(sql)
    d.commit()
    print('Data Updated..')
except Exception as ex:
    print(ex)
d.close()





import pymysql
try:
    d=pymysql.connect(host='localhost',user='root',password='Cloud@123$',db='fis')

    cur=d.cursor()
    sql="create table test(empno int,name varchar(20))"

    cur.execute(sql)
    d.commit()
    print('Table Created..')
except Exception as ex:
    print(ex)
d.close()






import pymysql
try:
    d=pymysql.connect(host='localhost',user='root',password='Cloud@123$',db='fis')

    cur=d.cursor()
    sql="drop table test"

    cur.execute(sql)
    d.commit()
    print('Table Deleted..')
except Exception as ex:
    print(ex)
d.close()





import pymysql
try:
    dd=pymysql.connect(host='localhost',user='root',password='Cloud@123$',db='fis')

    cur=dd.cursor()
    a=int(input('Enter Empno...'))
    b=input('Enter Name...')
    c=input('Enter City...')
    d=int(input('Enter Salary...'))
    sql="insert into employee values(%d,'%s','%s',%d)"%(a,b,c,d)

    cur.execute(sql)
    dd.commit()
    print('Data Inserted..')
except Exception as ex:
    print(ex)
dd.close()





import pymysql
try:
    dd=pymysql.connect(host='localhost',user='root',password='Cloud@123$',db='fis')

    cur=dd.cursor()
    a=int(input('Enter Empno...'))
    sql1="select empno from employee"
    cur.execute(sql1)
    data=cur.fetchall()
    if a!=0:
        for res in data:
            if res[0]==a:
                print('Empno already present....')
        else:
            b=input('Enter Name...')
            c=input('Enter City...')
            d=int(input('Enter Salary...'))
            sql="insert into employee values(%d,'%s','%s',%d)"%(a,b,c,d)
            cur.execute(sql)
            print('Data Inserted..')
    dd.commit()
except Exception as ex:
    print(ex)
dd.close()


'''
























