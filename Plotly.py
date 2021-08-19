#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.express as px
fig=px.line(x=[1,2,3],y=[1,2,3])
fig.show()


# In[2]:


import plotly.express as px
fig=px.line(x=[12,21,13])
fig.show()


# In[3]:


import plotly.express as px
fig=px.line(y=[12,21,13])
fig.show()


# In[5]:


import plotly.express as px
names=['raj','ravi','amit']
sal=[43000,91000,32000]
fig=px.line(x=names,y=sal)
fig.show()


# In[6]:


names=['raj','ravi','amit']
sal=[43000,91000,32000]
fig=px.bar(x=names,y=sal)
fig.show()


# In[7]:


import pandas as pd
import plotly.express as px
d={'rollno':[101,102,103,104],'name':['a','b','c','d'],'marks':[43,67,87,91]}
df=pd.DataFrame(d)
fig=px.scatter(x=df['name'],y=df['marks'])
fig.show()


# In[8]:


import pandas as pd
import plotly.express as px
d={'rollno':[101,102,103,104],'name':['a','b','c','d'],'marks':[43,67,87,91]}
df=pd.DataFrame(d)
fig=px.pie(df,values=df['marks'],names='name')
fig.show()


# In[ ]:




