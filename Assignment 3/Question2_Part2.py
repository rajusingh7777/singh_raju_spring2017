
# coding: utf-8

# # Question2_Part2
# 
# - Data contains fiscal and calendar year information. Same employee details exist twice in the dataset. Filter data by calendar year and find average salary (you might have to find average for each of the columns for every employee. Eg. Average of Total Benefits, Average of total compensation etc.) for every employee.
# - Now, find the people whose overtime salary is greater than 5% of salaries (salaries refers to ’Salaries' column)
# - For each ‘Job Family’ these people are associated with, calculate the percentage of total benefits with respect to total compensation (so for each job family you have to calculate average total benefits and average total compensation). Create a new column to hold the percentage value. 
# - Displaythe top 5 Job Families according to this percentage value usingdf.head().
# - Write the output (jobs and percentage value) to a csv.

# In[1]:

import pandas as pd #importing pandas


# In[2]:

df=pd.read_csv('Data/employee_compensation.csv') #reading csv file


# In[3]:

df.columns=df.columns.str.replace(' ','_') #replacing all space in column's name by _


# In[4]:

df1=df[df.Year_Type=='Calendar'] #filter out Fiscal from Year_Type column


# In[5]:

#Sol of 1st section of the question: Avg of Salaries of all employees
df_new=df1.groupby(['Job_Family','Employee_Identifier']).agg({'Salaries':'mean','Overtime':'mean','Other_Salaries':'mean','Total_Salary':'mean','Retirement':'mean','Health/Dental':'mean','Other_Benefits':'mean','Total_Benefits':'mean','Total_Compensation':'mean'})
df_new.reset_index(inplace=True)


# In[6]:

#Sol of 2nd section of the question: Overtime >=5% Salaries for all employee
df_new1=df_new[df_new.Overtime > df_new.Salaries*.05]


# In[7]:

#Sol of 3rd section of the question: % of total benefit to total compensation
df_new2=df_new1.groupby(['Job_Family']).agg({'Total_Benefits':'mean','Total_Compensation':'mean'})
df_new2['Percent_Total_Benefit']=df_new2.Total_Benefits/df_new2.Total_Compensation*100


# In[8]:

#Reindex and rename columns
df_new2.reset_index(inplace=True)
df_new2.columns=['Job Family','Total Benefits','Total Compensation','Percent_Total_Benefit']
df_new3=df_new2.sort_values('Percent_Total_Benefit', ascending =False)
print(df_new3.head())


# In[9]:

#Sol of 4th section of question: writing to csv file
df_new3.to_csv('Question2_Part2.csv', index=False)

