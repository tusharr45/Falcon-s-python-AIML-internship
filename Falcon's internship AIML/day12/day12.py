import pandas as pd
s=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print(s)
print(type(s))

# series is asingle dimentional labelled data structure 
ss=pd.Series([1,2,3,4,5])
print(ss)
print(type(s))


# d=pd.Series({"one":10,"two":20,"three":30},index={'one','two','three','a','b','c'})
# print(d)
# print(type(d))

# extraxct element 
'''
a=pd.Series([1,2,3,4,5,6])

b=pd.Series([11,12,13,14,15,16])

print(a[4])
print(a[-3])
print(a[:5])

# addition
print(a+10)
print(a+b)


# Dataframe => Two dimensional labelled data structure 

import pandas as pd 
data=pd.DataFrame({"name":["radha","krishna"],"marks"[100,200]})


'''

# read any csv file

import pandas as pd
data = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
print(data)
data.describe
data.shape
data.iloc[5:9 ,1:3]

# locaion 

# data.loc[0:3,('sepal_lengh','petal_width','species')]


# dropan data
data.drop([128,121,123],axis=0)
data.iloc[120:125,:].head()

data.drop([1,2,3],axis=0)

# for shape of file 
data.shape



import pandas as pd

data=pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

data


data.head()

data.tail()

data.shape

data.describe()

data

data.iloc[5 : 9 , 1 :3]

data.loc[0:3,('sepal_length','petal_width'	,'species' )]

data.drop('petal_width' , axis=1)


# minimum row and column facth in iloc 
data.iloc[ 120: 130 ,: ].head()

ans=data.drop([120,121,123], axis=0)
print(ans)
#data.iloc[ 120: 130 ,: ].head()

# data.iloc[ 115: 125 ,: ].head()


ans=data.drop([1,2,3], axis=0)

print(ans.shape)

print(data.shape)

data.shape



ans=data.drop([120,122,123], axis=0)

ans.iloc[ 115 : 130 , ]

data.min()

data.max()

data.median()

