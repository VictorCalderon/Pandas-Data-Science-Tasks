# Pandas and NetworkX Data Science Tasks
Set of real world data science tasks completed using the Python Pandas library.

## Disclaimer
Original dataset, questions and part of this README.md file froked from: KeithGalli/Pandas-Data-Science-Tasks.

Check out Keith's first video on Pandas: <br/>
https://youtu.be/vmEHCJofslg 

Check out the videos Keith did on Matplotlib: <br/>
https://youtu.be/DAQNHzOcO5A <br/>
https://youtu.be/0P7QnIQDBJY

## Setup
To replicate these analyses the following libraries are needed: 

1. Pandas
2. NetworkX
3. Seaborn

## Background Information:
In this notebook we analyze and answer business questions about 12 months worth of sales data. The data contains hundreds of thousands of electronics store purchases broken down by month, product type, cost, purchase address, etc. 

We start by cleaning our data. Tasks during this section include:
- Drop NaN values from DataFrame
- Removing rows based on a condition
- Change the type of columns (to_numeric, to_datetime, astype)

Once we have cleaned up our data a bit, we move the data exploration section. In this section we explore 5 high level business questions related to our data:
- What was the best month for sales? How much was earned that month?
- What city sold the most product?
- What time should we display advertisemens to maximize the likelihood of customer’s buying product?
- What products are most often sold together?
- What product sold the most? Why do you think it sold the most?
