'''

import pandas as pd
df=pd.read_csv('salaries.csv')
print(df)





import pandas as pd
df=pd.read_csv('salaries.csv')
#head top 5 records
print(df.head())



import pandas as pd
df=pd.read_csv('salaries.csv')
#head top 2 records
print(df.head(2))




import pandas as pd
df=pd.read_csv('salaries.csv')
#tail bottom 5
print(df.tail())




import pandas as pd
df=pd.read_csv('salaries.csv')
#tail bottom 3
print(df.tail(3))





import pandas as pd
df=pd.read_csv('salaries.csv')
print(df.dtypes)




import pandas as pd
df=pd.read_csv('salaries.csv')
print(df)
#no of rows and cols
print(df.shape)





import pandas as pd
df=pd.read_csv('salaries.csv')
print(df)
print(df[0:3]) #rows 0 to 2
print(df[4:]) #row 4 onwards




import pandas as pd
df=pd.read_csv('salaries.csv')
print(df.iloc[0:2,0:3])



import pandas as pd
df=pd.read_csv('salaries.csv')
#conditional data
dt=df[(df['salary']>90000)]
print(dt)




import pandas as pd
df=pd.read_csv('salaries.csv')
#conditional data
dt=df[(df['salary']>90000) & (df['discipline']=='B')]
print(dt)




import pandas as pd
df=pd.read_csv('salaries.csv')
#Handling missing values

df['service'].fillna('0',inplace=True)
print(df)





import pandas as pd
df=pd.read_csv('salaries.csv')
#Handling missing values
#replace by sum,max,min value
df['service'].fillna(df['service'].sum(),inplace=True)
print(df)


import pandas as pd
df=pd.read_csv('salaries.csv')
#Handling missing values
#replace by sum,max,min value
df['service'].fillna(df['service'].max(),inplace=True)
print(df)


import pandas as pd
df=pd.read_csv('salaries.csv')
#Handling missing values
#replace by sum,max,min value
df['service'].fillna(df['service'].min(),inplace=True)
print(df)




import pandas as pd
df=pd.read_csv('salaries.csv')
#all null removed
dt=df.dropna()
print(dt)





import pandas as pd
df=pd.read_csv('salaries.csv')
#insert new column
df.insert(6,'test',df['service']+20)
print(df)




import pandas as pd
df=pd.read_csv('salaries.csv')
df1=pd.read_csv('salaries1.csv')
df2=df.append(df1)
print(df2)





import pandas as pd
df=pd.read_csv('Emp.csv')
df1=pd.read_csv('EmpGrade.csv')
print(pd.merge(df,df1,on='EmpNo'))





import pandas as pd
df=pd.read_csv('salaries.csv')
#sorted data--asscending
print(df.sort_values('salary'))




import pandas as pd
df=pd.read_csv('salaries.csv')
#sorted data--descending
print(df.sort_values('salary',ascending=False))




import pandas as pd
df=pd.read_csv('salaries.csv')
#group on base of rank and sum of salary
dc=df.groupby(['rank'])
print(dc['salary'].sum())





import pandas as pd
df=pd.read_csv('StudentDataForPivot.csv')
print(pd.pivot_table(df,index=['Name','Subject'],
                     values='Score',aggfunc='sum'))





import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('EmpData.csv')
plt.plot(df['EmpCode'],df['Payment'],color='red',
         linestyle='--',linewidth=5)
plt.show()




import pandas as pd
#import matplotlib.pyplot as plt
df=pd.read_csv('EmpData.csv')
dfg=df.groupby("City")
total=dfg['Payment'].sum()
total.plot(kind='bar')





import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('EmpData.csv')
plt.hist(df['Payment'],bins=5)
plt.show()




import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('EmpData.csv')
c=df.groupby(df['City'])
cp=['red','green','blue']
c.sum().plot(kind='pie',y='Payment')

'''


import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('EmpData.csv')

plt.scatter(df['Payment'],df['NoOfHours'],marker='o')
plt.show()





