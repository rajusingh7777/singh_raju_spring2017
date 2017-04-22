# ANALYSIS PATTERN- 2 (API to collect data and store + 3 Analysis 


# PROBLEM STATEMENT
![alt tag](http://..//images/1.png)
To collect and store data through API and perform any 3 analysis on any dataset.
I have taken Boston Crime Dataset from a government website- https://data.cityofboston.gov/


# DATA PROCESSING

Data calling:



Data Storage:
There were two crime database one from 2012 to 2015 (Legacy) and another one from 2015 to 2017.
The way Boston government store crime data in former is different from the Legacy period.
Two Database columns' header and data were slightly different. I renamed the columns of both and named them as same.
And merge two database together based on common columns name.
However, while calling data for analysis, I need to put 'or' condition inorder to get data from both legacy and latest merged database  


