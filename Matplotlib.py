'''

import matplotlib.pyplot as plt
x=[10,22,35]
y=[20,10,25]
plt.plot(x,y)
plt.show()




import matplotlib.pyplot as plt
x=[10,22,35]
y=[20,10,25]
plt.plot(x,y,'--r')
plt.show()




import matplotlib.pyplot as plt
x1=[10,22,35]
y1=[20,10,25]
plt.plot(x1,y1,'--r')
x2=[11,23,31]
y2=[20,24,32]
plt.plot(x2,y2,'--g')
plt.show()





import matplotlib.pyplot as plt
states=['Delhi','AP','MP']
pop=[1.2,4.9,3.8]
plt.plot(states,pop)
plt.title('Pop in Crore')
plt.xlabel("States")
plt.ylabel("Population")
plt.show()






import matplotlib.pyplot as plt
sem=[1,2,3,4,5,6,7,8]
m1=[34,90,65,37,87,96,75,84]
m2=[54,76,43,58,99,30,58,48]
plt.plot(sem,m1,label='Raj')
plt.plot(sem,m2,label='Amit')
plt.legend()
plt.xlabel("Semester")
plt.ylabel("Marks")
plt.show()




import matplotlib.pyplot as plt
sem=[1,2,3,4,5,6,7,8]
m1=[34,90,65,37,87,96,75,84]

plt.bar(sem,m1)
plt.title('Bar Chart...')
plt.show()





import matplotlib.pyplot as plt
esem=[2,4,6,8]
osem=[1,3,5,7]
m1=[34,90,65,37]
m2=[87,96,75,84]

plt.bar(esem,m1,color='r')
plt.bar(osem,m1,color='g')
plt.title('Bar Chart...')
plt.show()





import pandas as pd
import matplotlib.pyplot as plt
d={'empno':[101,102,103,104],'name':['Amit','Vivek','Raj','Ram'],
   'salary':[4300,6700,8700,9100]}
df=pd.DataFrame(d)
print(df)
df['tax']=df['salary']*0.3
print(df)
plt.bar(df['name'],df['tax'])







import matplotlib.pyplot as plt
import numpy as np

ct=['India','USA','UK']
pop=[1.35,1.80,1]
y=np.arange(len(ct))

plt.bar(y,pop)
plt.xticks(y,ct)
plt.title('Pop Chart')
plt.show()




import matplotlib.pyplot as plt
import numpy as np

ct=['India','USA','UK']
pop=[1.35,1.80,1]
y=np.arange(len(ct))

plt.barh(y,pop)
plt.xticks(y,ct)
plt.title('Pop Chart')
plt.show()






import matplotlib.pyplot as plt
x=[2,4,6,8]
y=[32,65,76,90]
plt.scatter(x,y)
plt.show()




import matplotlib.pyplot as plt
ages=[32,65,23,18,19,45,65,54,51,31]
plt.hist(ages,bins=5)
plt.show()




import matplotlib.pyplot as plt
labels='UP','MP','AP','Delhi'
lit=[25,35,45,65]
col=['green','red','yellow','blue']
e=(0,0,0,0.1)
plt.pie(lit,explode=e,labels=labels)
plt.show()






import pandas as pd
data={'unemployement':[4.3,3.6,7.1,4.1,8.9,9.0,12.3],
      'MarketShare':[1200,1100,300,1300,800,910,1811]}
df=pd.DataFrame(data,columns=['unemployement','MarketShare'])
print(df)
df.plot(x='unemployement',y='MarketShare',kind='scatter')





import pandas as pd
data={'year':[1971,1981,1991,2001,2011],
      'pop':[50,72,81,98,111]}
df=pd.DataFrame(data,columns=['year','pop'])
df.plot(x='year',y='pop',kind='line')






import pandas as pd
data={'country':['India','US','UK'],'gdp':[5,9,8]}
df=pd.DataFrame(data,columns=['country','gdp'])
df.plot(x='country',y='gdp',kind='bar')





import pymysql
import matplotlib.pyplot as plt
d=pymysql.connect(host='localhost',user='root',password='Cloud@123$',db='fis')

cur=d.cursor()
sql="select ename,salary from employee"

cur.execute(sql)
data=cur.fetchall()
a=[]
b=[]
for res in data:
    a.append(res[0])
    b.append(res[1])
plt.bar(a,b)
plt.show()
d.close()


'''




