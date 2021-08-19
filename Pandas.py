'''

import pandas as pd
#series
#blank series
s=pd.Series()
print(s)





import pandas as pd
#series with values
s=pd.Series([32,54,1,90])
print(s)




import pandas as pd
#series with values
s=pd.Series(['p','x','k','r'])
print(s)





import pandas as pd
#series with values and index
s=pd.Series(['p','x','k','r'],index=[121,190,321,87])
print(s)



import pandas as pd
#series with values
s=pd.Series([32,54,1,90],index=['p','x','k','r'])
print(s)





import pandas as pd
#series with values
s=pd.Series([32,54,1,90],index=['p','x','k','r'])
print(s)
#index for search
print(s['x'])





import pandas as pd
#dictionary
st={'rollno':101,'name':'Pooja','city':'Delhi','marks':91}
s=pd.Series(st)
print(s)



import pandas as pd
#dictionary
st={'rollno':101,'name':'Pooja','city':'Delhi','marks':91}
s=pd.Series(st,index=['city','name','rollno','marks'])
print(s)




import pandas as pd
#scalar series
s=pd.Series(8,index=['x','a','b','p','k'])
print(s)





import pandas as pd
#blank dataframe
df=pd.DataFrame()
print(df)




import pandas as pd
d=[32,5,76,90,121,4]
#it shows in 2D format
df=pd.DataFrame(d)
print(df)





import pandas as pd
d=[['amit',21],['raj',23],['vivek',19],['ravi',31]]
df=pd.DataFrame(d,columns=['Name','Age'])
print(df)




import pandas as pd
d={'rollno':[101,102,103,104],'name':['a','b','c','d'],'marks':[43,67,87,91]}
df=pd.DataFrame(d,index=['rank1','rank2','rank3','rank4'])
print(df)




import pandas as pd
d={'rollno':[101,102,103,104],'name':['a','b','c','d'],'marks':[43,67,87,91]}
df=pd.DataFrame(d,index=['rank1','rank2','rank3','rank4'])
print(df)
print(df['rollno'])
df['promote']=df['marks']+10
print(df)




import pandas as pd
d={'empno':[101,102,103,104],'name':['a','b','c','d'],
   'basic':[43,67,87,91]}
df=pd.DataFrame(d,index=['rank1','rank2','rank3','rank4'])
print(df)
df['HRA']=df['basic']*0.12
df['total']=df['basic']+df['HRA']
print(df)


'''









