
# coding: utf-8

# # Question4_Part1
# 
# - Use ‘movies_awards’ data set.
# - You are supposed to extract data from the awards column in this dataset and split it into several columns. An example is given below.
# - The awards has details of wins, nominations in general and also wins and nominations in certain categories(e.g. Oscar, BAFTA etc.)
# - You are supposed to create a win and nominated column (these 2 columns contain total number of wins and nominations) and other columns that extract the number of wins and nominations for each category of award. 
# - If a movie has 2 Oscar nominations and 4 Oscar won, the columns Oscar_Awards_Won should have value 4 and Oscar_Awards_Nominated should have value 2. You should also have a total won and nominated column which aggregates all the awards (won or nominated). 
# - Create two separate columns for each award category (won and nominated).
# - Write your output to a csv file. (Sample output is given in next page)

# In[1]:

import pandas as pd #importing pandas


# In[2]:

df=pd.read_csv('Data/movies_awards.csv') #reading csv file


# In[3]:

df=df[df.Awards.notnull()] #filtering out the NaN value in Awards column
df=df.reset_index(drop=True) #resetting index


# In[4]:

#Selecting column Awards for analysis
df1=df.ix[:,['Awards']]


# In[5]:

#Creating Column Awards_won and adding values to it
import re

df1['Awards_won']=df1.Awards.apply(lambda x:(int(re.findall(r"(\d+) win",x)[0])  # finding digits which preceded win
                                             if len(re.findall(r"(\d+) win",x))!=0 else 0) 
                                   + (int(re.findall(r"Won (\d+)",x)[0])         # finding digits which succeeded Won
                                      if len(re.findall(r"Won (\d+)",x))!=0 else 0))


# In[6]:

#Creating Column Awards_nominated and adding values to it
df1['Awards_nominated']=df1.Awards.apply(lambda x:(int(re.findall(r"(\d+) nom",x)[0]) # finding digits which preceded nom
                                                   if len(re.findall(r"(\d+) nom",x))!=0 else 0)
                                        + (int(re.findall(r"Nominated for (\d+) Pri",x)[0]) # finding digits which contains in 'Nominated for _ Pri'
                                           if len(re.findall(r"Nominated for (\d+) Pri",x))!=0 else 0)
                                        + (int(re.findall(r"Nominated for (\d+) Osc",x)[0])
                                           if len(re.findall(r"Nominated for (\d+) Osc",x))!=0 else 0)
                                        + (int(re.findall(r"Nominated for (\d+) Gol",x)[0])
                                           if len(re.findall(r"Nominated for (\d+) Gol",x))!=0 else 0)
                                        + (int(re.findall(r"Nominated for (\d+) BAFTA",x)[0])
                                           if len(re.findall(r"Nominated for (\d+) BAFTA",x))!=0 else 0))


# In[7]:

#Creating Columns and adding values to them
df1['Prime_Awards_nominated']=df1.Awards.apply(lambda x:(int(re.findall(r"Nominated for (\d+) Pri",x)[0])
                                                          if len(re.findall(r"Nominated for (\d+) Pri",x))!=0 else 0))
df1['Oscar_Awards_nominated']=df1.Awards.apply(lambda x:(int(re.findall(r"Nominated for (\d+) Osc",x)[0])
                                                          if len(re.findall(r"Nominated for (\d+) Osc",x))!=0 else 0))
df1['Golden_Globe_Awards_nominated']=df1.Awards.apply(lambda x:(int(re.findall(r"Nominated for (\d+) Gol",x)[0])
                                                                if len(re.findall(r"Nominated for (\d+) Gol",x))!=0 else 0))
df1['BAFTA_Awards_nominated']=df1.Awards.apply(lambda x:(int(re.findall(r"Nominated for (\d+) BAFTA",x)[0])
                                                         if len(re.findall(r"Nominated for (\d+) BAFTA",x))!=0 else 0))


# In[8]:

#Creating Columns and adding values to them
df1['Prime_Awards_won']=df1.Awards.apply(lambda x:(int(re.findall(r"Won (\d+) Pri",x)[0])
                                                   if len(re.findall(r"Won (\d+) Pri",x))!=0 else 0))
df1['Oscar_Awards_won']=df1.Awards.apply(lambda x:(int(re.findall(r"Won (\d+) Osc",x)[0])
                                                   if len(re.findall(r"Won (\d+) Osc",x))!=0 else 0))
df1['Golden_Globe_Awards_won']=df1.Awards.apply(lambda x:(int(re.findall(r"Won (\d+) Gol",x)[0])
                                                          if len(re.findall(r"Won (\d+) Gol",x))!=0 else 0))
df1['BAFTA_Awards_won']=df1.Awards.apply(lambda x:(int(re.findall(r"Won (\d+) BAFTA",x)[0])
                                                   if len(re.findall(r"Won (\d+) BAFTA",x))!=0 else 0))


# In[9]:

print(df1.head())


# In[10]:

df1.to_csv('Question4_Part1.csv', index=False) #populate to csv without index

