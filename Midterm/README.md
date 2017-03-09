# Question 1: Analysis of Enron scandal:

- Summary about the scandal

Enron Corp. is a company that reached dramatic heights, only to face a dizzying collapse. The story ends with the bankruptcy of one of America's largest corporations.Enron's collapse affected the lives of thousands of employees and shook Wall Street to its core. At Enron's peak, its shares were worth $90.7 but fter the company declared bankruptcy on December 2, 2001, they plummeted to $0.67 by January 2002

Analysis 1:

Finding CEO Jeff Skilling getting most mail from and sent-to by him.

Analaysis-1 result


Top email sent by CEO Jeffery Skilling:
---------------------------------------
jeff.skilling@enron.com
None
smu-betas@yahoogroups.com
jskilli@enron.com
markskilling@hotmail.com
jeff.skilling@enron.com, etblaw@aol.com, gbsmith@smith-graham.com, rcampos@eldoradocorp.com, shirley.h.tapscott@uth.tmc.edu


Top email recieved to CEO Jeffery Skilling:
---------------------------------------
sherri.sera@enron.com
joannie.williamson@enron.com
markskilling@hotmail.com
40enron@enron.com
fredinvt@juno.com

Based on above data we can start investigation who other people are involved in it.

Analysis 2:

Find the top 10 words of CEO Jeffery Skilling in his email directory:

Top 10 words in the CEO email are:
morgangroup.com
morgan
diego
san
jeff
enron
ronnie
chapter
michaelm
enron.com

The top words may give clue about the conversation happening with him.

Analysis 3:
Finding the number of mails dropped on each days of a given sample data (5000 emails).


Of sample size of 5000 mails, we found that-
1. Mail sent by enron employees on Mon: 1089
2. Mail sent by enron employees on Tue: 1040
3. Mail sent by enron employees on Wed: 1035
4. Mail sent by enron employees on Thu: 893
5. Mail sent by enron employees on Fri: 763
6. Mail sent by enron employees on Sat: 74
7. Mail sent by enron employees on Sun: 106

It is little unusal to have mail on weekend. So, we can have our investigation start from Sunday which is also low in volume to go through




# Question 2: Storage and Analysis of New York Times paper.

Data Storage:
1. API Key generated.
2. Set the key as environment variable.
3. Query set to get desire page is set.
4. One page per day of desired query is fetch for required duration
5. Store the page as JSON format at local dirve.
6. All data for three analysis is stored in seperate folders.

Analysis 1
1. To check the popularity Hillary and Trump in term of news paper bytes.
2. Since page stored with dates, I used dates to map each presidential candidates received coverage in news paper.
3. It is observed that Hiallary was initially popular but as election days progressed Trump recieved more coverage.

We can refer csv file and can see that Trump start getting more coverage post 15-Aug and since then he got most coverage.


Analysis 2
1. Finding top 5 words get most attention in the US election campaing from 1 Aug 2016 till 7 Now 2016 i.e. before election day
2. A dictionary was created for popular issues that were given most attention in US election.
3. Then the dictornary items was iterate over parsed JSON file to find such number of such words.
4. Sorted the new dictionary with all key and values and found the top 5 issue that played imported role in election campain

Top 5 words in the US election campaing are:
russia
immigration
china
job
hacking


Analysis 3
1. Finding top 5 words sports mostly covered in NYT in last 6 months
2. A dictionary was created for popular sports played in the USA.
3. Then dictornary items was iterate over parsed JSON file to find such number of words.
4. Sorted the new dictionary with all key and values of sports and found the top 5 sports covarage

Top sports covered in last 6 months in US, down the order:
football
soccer
basketball
baseball
tennis
