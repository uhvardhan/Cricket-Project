# Decision Review System (DRS) data analysis - IPL 2024

### Background
The Decision Review System (DRS) is a technology-based process to assist on-field match officials with their decision-making.
Team captains may request that the third umpire consider a decision of the on-field umpires also known as Team review. Each
team is limited to 2 unsuccessful reviews per innings.

### Data Collection
The data has been collected from ESPNCricinfo - Match Flow section. Here is an example of Match 31: [Kolkata Knight Riders vs Rajasthan Royals](https://www.espncricinfo.com/series/indian-premier-league-2024-1410320/kolkata-knight-riders-vs-rajasthan-royals-31st-match-1426269/full-scorecard)

### Data Science Process
Step 1: Ask an interesting question.
        (i)   What is the goal?
        (ii)  What would you do if you had all the data?
        (iii) What do you want to predict or estimate?
Step 2: Get the data.
        (i)   How were the data sampled?
        (ii)  Which data are relevant?
        (iii) Are there any privacy issues?
Step 3: Explore the data.
        (i)   Plot the data
        (ii)  Are there anomalies
        (iii) Are there patterns?
Step 4: Model the data.
        (i)   Build a model.
        (ii)  Fit the model.
        (iii) Validate the model.
Step 5: Communicate and visualize the results.
        (i)   What did we learn?
        (ii)  Do the results make sense?
        (iii) Can we tell a story?

### Required Libraries:
1. Python
2. Pandas
3. Seaborn
4. Matplotlib
5. BeautifulSoup4 (for data extraction)

### Questions answered:
1. Day 1: Total number of reviews taken in each innings.
2. Day 2: Total number of reviews taken in each over.
3. Day 3: Total number of reviews taken per type.
4. Day 4: Total number of reviews taken by batting or fielding sides.
5. Day 5: Total number of reviews taken per umpire.
6. Day 6: Total number of reviews taken in each match.
7. Day 7: Total number of reviews taken per team and Number of successful/unsuccessful reviews by each team.

### Future work:
1. How has the trend of review taking changed over the course of the season?
2. Running average number of reviews over the course of the season?
3. 