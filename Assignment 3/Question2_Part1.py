
# coding: utf-8

# # Question2_Part1
# - Use 'employee_compensation' data set.
# - Find out the highest paid departments in each organization group by calculating mean of total compensation for every department.
# - Output should contain the organization group and the departments in each organization group with the total compensationfrom highest to lowest value.
# - Display a few rows of the outputuse df.head().
# - Generate a csv output.

# In[1]:

import pandas as pd #importing pandas


# In[2]:

df=pd.read_csv('Data/employee_compensation.csv') #reading csv file


# In[3]:

df1=df.loc[:,('Organization Group','Department','Total Compensation')] #selecting required columns for analysis


# In[4]:

df1.columns=df1.columns.str.replace(' ','_') #replacing all space in column's name by _


# In[5]:

x= df1.groupby(['Organization_Group','Department']).Total_Compensation.mean() #groupby two columns and calu. mean
df_new=pd.DataFrame({'Total_Compensation':x}) #new datafram created
df_new.reset_index(inplace=True) #index reset


# In[6]:

#sorted by Organization_Group & Total_Compensation column
df_new1=df_new.sort_values(['Organization_Group','Total_Compensation'],ascending=[True,False])
df_new1.columns=['Organization Group','Department','Total Compensation'] #rename columns as per requirement
print(df_new1.head())


# In[7]:

df_new1.to_csv('Question2_Part1.csv', index=False) #setting index false from being populated in csv

