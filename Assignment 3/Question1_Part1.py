
# coding: utf-8

# # Question1_Part1
# 
# - Use ‘vehicle_collisions’ data set.
# - For each month in 2016, find out the percentage of collisions in Manhattan out of that year's total accidents in New York City.
# - Display a few rows of the outputuse df.head().
# - Generate a csv output with four columns (‘Month’, ‘Manhattan’, ‘NYC’, ‘Percentage’)

# In[1]:

import pandas as pd #importing pandas


# In[2]:

df=pd.read_csv('Data/vehicle_collisions.csv') #reading csv file


# In[3]:

df['DATE']=pd.to_datetime(df.DATE) # coverting datatype of column 'Date' from object type to datetime64[ns] type


# In[4]:

df=df[pd.to_datetime('1/1/16')<=df.DATE] #selecting rows with date equal or greater than 01- Jan-2016
df=df[df.DATE<=pd.to_datetime('12/31/16')] #selecting rows with date equal or less than 31- Dec-2016
df1=df.ix[:,('DATE','BOROUGH')] #working with two columns Date and Borough


# In[5]:

df1['MONTH_Num']=df1.DATE.dt.month  #new column Month added. It will have month name as its value.
#df1['MONTH']=df1.DATE.dt.strftime('%B')


# In[6]:

x=df1[df1.BOROUGH=='MANHATTAN'].groupby('MONTH_Num').BOROUGH.count() #new variable created with value as group by month for Borough='MANHATTAN
y=df1.groupby('MONTH_Num').DATE.count() #new variable created with value as group by month for all entries count of Borough
z=x/y #percentage count


# In[7]:

new_df=pd.DataFrame({'MANHATTAN':x,'NYC':y,'PERCENTAGE':z}) #new dataframe created with above variable values


# In[8]:

new_df.reset_index(inplace=True) #resetting index
#Mapping MONTH_Num column to MONTH
new_df['MONTH']=new_df.MONTH_Num.map({1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun', 7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'})
new_df1=new_df.loc[:,('MONTH','MANHATTAN','NYC')] #Calling required columns
print(new_df1.head())


# In[9]:

new_df1.to_csv('Question1_Part1.csv', index = False) #setting index false from being populated in csv

