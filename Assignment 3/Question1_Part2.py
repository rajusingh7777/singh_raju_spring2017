
# coding: utf-8

# # Question1_Part2
# 
# - Use ‘vehicle_collisions’ data set.
# - For each borough, find out distribution of each collision scale. (One car involved? Two? Three? or more?) (From 2015 to present)
# - Display a few rows of the outputuse df.head().
# - Generate a csv output with five columns ('borough', 'one-vehicle', 'two-vehicles', 'three-vehicles', 'more-vehicles')

# In[1]:

import pandas as pd #importing pandas


# In[2]:

df=pd.read_csv('Data/vehicle_collisions.csv') #reading csv file


# In[3]:

# call columns which are required for analysis
df1=df.ix[:,('BOROUGH','VEHICLE 1 TYPE','VEHICLE 2 TYPE','VEHICLE 3 TYPE','VEHICLE 4 TYPE', 'VEHICLE 5 TYPE')]


# In[4]:

#Counting across columns i.e. axis=1 for 'VEHICLE X TYPE' columns
df1['VEHICLES_INVOLVED']=df1.loc[:,('VEHICLE 1 TYPE','VEHICLE 2 TYPE','VEHICLE 3 TYPE','VEHICLE 4 TYPE',
                                    'VEHICLE 5 TYPE')].count(axis=1,level=None,  numeric_only=False)


# In[5]:

df2=df1.groupby(['BOROUGH','VEHICLES_INVOLVED']).VEHICLES_INVOLVED.count() #groupby borough and vehicles_involved
df3=pd.DataFrame({'Count1':df2})
df3.reset_index(inplace=True)


# In[6]:

df4=df3.pivot(index='BOROUGH', columns='VEHICLES_INVOLVED', values='Count1') #pivoted the index, columns and values
df4.columns=['ZERO_VEHICLE_INVOLVED','ONE_VEHICLE_INVOLVED','TWO_VEHICLES_INVOLVED',
           'THREE_VEHICLES_INVOLVED','FOUR_VEHICLES_INVOLVED','FIVE_VEHICLES_INVOLVED'] #rename the columns


# In[7]:

df4['MORE_VEHICLES_INVOLVED']=df4.FOUR_VEHICLES_INVOLVED+df4.FIVE_VEHICLES_INVOLVED #New column added
df4=df4.loc[:,('ONE_VEHICLE_INVOLVED','TWO_VEHICLES_INVOLVED','THREE_VEHICLES_INVOLVED','MORE_VEHICLES_INVOLVED')]
df4.reset_index(inplace=True)


# In[8]:

print(df4.head())


# In[9]:

df4.to_csv('Question1_Part2.csv',index=False) #setting index false from being populated in csv

