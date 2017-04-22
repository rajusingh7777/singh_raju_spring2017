# ANALYSIS PATTERN- 2 (API to collect data and store + 3 Analysis 


# PROBLEM STATEMENT
![topic_analysis](images/1.png)
To collect and store data through API and perform any 3 analysis on any dataset.
I have taken Boston Crime Datasets from a government website- https://data.cityofboston.gov/ and perform three analysis on the them. In order to support further arugument in analysis, I have added a new dataset hosted on the same website.


# DATA PROCESSING

# Data calling:

Boston data.cityofboston.gov/ website through Socrata, facilitates open data API for developer to gather the data. Getting data through API has less throttling compared to directly access the data for a particular ip address.

![api_request1](images/2.png)
![api_request2](images/3.png)

All datasets have a unique identifier - eight alphanumeric characters split into two four-character phrases by a dash.

For example, ufcx-3fdn is the identifier for the Boston crime data 2012 to 2015 (Legacy format).

For gatherdata I have stored API key as environment variable using below command in the Terminal:
$ export BOSTON_API_KEY=xyzabcxyzabc111 (example only)


All files collected, through API, from the host are in json format appended with datetime as prefix to avoid replacing of the collected data. 


# Data Storage:

There were two crime database one from 2012 to 2015 (Legacy) and another one from 2015 to 2017.
The way Boston government store crime data in former is different from the Legacy ones.
Two Database columns' header and data were slightly different. I've renamed the columns header of both and named them as same and merge two database together based on common columns name.

However, while calling data for analysis, I need to put 'or' condition inorder to get data from both legacy and latest merged database in which values are stored slight differently.

All raw data filea are stored in 'data' folder.

Further, for the analysis I have dumped all json files into a consolidated csv file. The consolidated csv files were put inside a  processedData which is inside 'data' folder only.

For all the analysis I have used the processed data only inorder to intact the json file as it and in any case of any eventuality I would be able to restored with the original raw data.

![data_store_str](images/4.png)


# ANALYSIS OF BOSTON CRIME


# Brief Introduction of Analysis-

# Objective of Analysis:
I have around six years of Boston crime records. I want to analyze the crime pattern of Boston over the six year and how crimes go change over the different neighborhood (Districts) of Boston.

# What are those Analysis:

1. 
2.
3.

# Conclusion of the Analysis:
Post Analysis we deduce the information that what and why certain crimes takes place on a particule day of a neighborhood (District) of Boston. Also, plottings have been done on Boston map to illustrate lucid pattern over different Boston's districts.  


# Details of the Analysis performed-


# Analysis 1:

1. Analysing the number of crime indicents in boston over the years.
2. Through pandas read csv function, access the processed data where merged crime database was placed.
3. Since, the database has data from Aug 2012 till Apr 2017, I have filtered out the year 2012 and 2017 from this analysis.
4. Thus, perfomed the anlysis on the crime incidents for year 2013 till 2016.
5. Done groupby over the year and count the crime incidents:

![incidents_byyear](images/a1.png)

Conclude that:
1. There is only subtle rise in crime over the years:

I take further dig into the data and check for which week the crime happened mostly:
1. I performed groupby function over the days of the week.
2. Ploted the crime against week

![incident_byweek](images/a2.png)

Conclude that:
1. Most crime reported on the Friday
2. Reason could be anything related with partying- intoxication and resulted behavior like vandalism but we cannot deduce the direct conclusion on this.


1. I now need to do further analysis to check the charges impressed upon the convict by police dept.
2. I checked the number of crime associated with drug, drink charges on the day of the week.
Note: A person can be charged with multiple complaints.
3. Filtered out the crime charge with drugs, drinks and realted likely event like vandalism.
4. Ploted the crime drugs/drinks/vandalism against days of the week.

![incident_byweek](images/a3.png)

Conclude that:
Drugs/drinks/vandalism related crime happened spike up on Friday.

Overall conclusion:
Crime incident in Boston over the year is subtle and when analyze crime incident by days, Friday comes out of the most voilent day of the week and reason could be drug/drinks and related crime action like vandalism which make up most of the crime number compared to other days of the week.  



# Analysis 2:


# Analysis 3:


# Addtional Instructions to Run the code:

1. I have added the basemap library which is an extension of matplotlib library to plot the data over geographical location of any part of the world based on Logitude and Latitude cordinates.

2. I have created seprate environment for this so that its installation does not interfer the existing conda environment. Open the terminal and copy the below code:

visualization_eq$ conda create -n eq_env python=3 matplotlib basemap pillow

3. To activate the envirnment copy below code:
source activate eq_env

4. In order to successfully import the basemap Install jupyter notebook on this environment as the earlier existing jupyter notebook would have installed on the default environment. 

Note: If any analysis on this environment requires supporting libraries to be installed, activate the enironment and installed the the library. 

Citation & Reference:
https://matplotlib.org/basemap/users/examples.html
http://introtopython.org/visualization_earthquakes.html












