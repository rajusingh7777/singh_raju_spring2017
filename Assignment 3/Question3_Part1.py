
# coding: utf-8

# # Question3_Part1
# 
# - Use ‘cricket_matches’ data set.
# - Calculate the average score for each team which host the game and win the game.
# - Remember that if a team hosts a game and wins the game, their score can be innings_1 runs or innings_2 runs. You have to check if the host team won the game, check which innings they played in (innings_1 or innings_2), and take the runs scored in that innings. The final answer is the average score of each team satisfying the above condition.
# - Display a few rows of the outputuse df.head()
# - Generate a csv output

# In[1]:

import pandas as pd #importing pandas


# In[2]:

df=pd.read_csv('Data/cricket_matches.csv') #reading csv file


# In[3]:

#call columns which is required for analysis
df1=df.ix[:,('match_details','home','winner','innings1','innings1_runs', 'innings2','innings2_runs')]


# In[4]:

df1=df1[df1.home==df1.winner] #to ensure winner is host


# In[5]:

x=df1.loc[df1.winner==df1.innings1,'innings1_runs'] #winner score who played first inning
y=df1.loc[df1.winner==df1.innings2,'innings2_runs'] #winner score who played second inning


# In[6]:

#New dataframe with column of first and in second inning correspondingly
df_new=pd.DataFrame({'home':df1.winner,'run_scored_innings1': x, 'run_scored_innings2': y})
df_new.fillna(0,inplace=True) #filling NaN by 0

df_new['Total_Score']=df_new.run_scored_innings1+df_new.run_scored_innings2 #new column created


# In[7]:

df_final=df_new.groupby('home').Total_Score.agg({'score':'mean'}) #groupby home and taken mean of Total_Score


# In[8]:

# resetting index from BOROUGH to default index
df_final.index.name='home'
df_final.reset_index(inplace=True)
print(df_final.head())


# In[9]:

df_final.to_csv('Question3_Part1.csv') #to populated csv

