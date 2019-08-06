#!/usr/bin/env python
# coding: utf-8



import pandas as pd
import numpy as np

dm=pd.read_csv('movies.csv')
print(dm.head(10))
print(dm.shape)
dg=dm.copy()


#spliting dates with movie name

x=dm['title'].str.partition('(',True)
x.head()
dm['title']=x[0]
dm['date']=x[2].str.replace(')','')
dg=dm.copy()
dg.to_csv('xyz.csv')


# In[8]:


#Using regular expressions to find a year stored between parentheses
#We specify the parantheses so we don't conflict with movies that have years in their titles
dm['year'] = dm.title.str.extract('(\(\d\d\d\d\))',expand=False)
#Removing the parentheses
dm['year'] = dm.year.str.extract('(\d\d\d\d)',expand=False)
#Removing the years from the 'title' column
dm['title'] = dm.title.str.replace('(\(\d\d\d\d\))', '')
#Applying the strip function to get rid of any ending whitespace characters that may have appeared
dm['title'] = dm['title'].apply(lambda x: x.strip())

dm.head()


cleaned=dm.set_index('title').genres.str.split('|',expand=True).stack()
df=pd.get_dummies(cleaned).groupby(level=0).sum()
df=df.drop('(no genres listed)',axis=1)
df.head()



de=dm.iloc[:,0:2]
de['year']=dm['year']
de.head()



dv=df.merge(de,how='inner',left_on='title',right_on='title').sort_values(by='movieId')

dmain=pd.DataFrame(dv)
dmain=dmain.reset_index(drop=True)
dmain.to_csv('movie_withgenres.csv')





