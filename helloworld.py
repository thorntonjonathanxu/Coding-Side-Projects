c = '''
Built-in Data Structures, Functions, and Files (42:33 mins)
NumPy Basics: Arrays and Vectorized Computation (50:36 mins)
Getting Started with pandas (46:00 mins)
Data Loading, Storage, and File Formats (33:21 mins)
Data Cleaning and Preparation (36:48 mins)
Data Wrangling: Join, Combine, and Reshape (35:39 mins)
Plotting and Visualization (42:33 mins)
Data Aggregation and Group Operations (41:24 mins)
Time Series (58:39 mins)
Advanced pandas (19:33 mins)
Introduction to Modeling Libraries in Python (25:18 mins)
Data Analysis Examples (64:24 mins)
Advanced NumPy (43:42 mins)
More on the IPython System (33:21 mins)
Index (72:27 mins)
'''
from datetime import datetime
import re

hour = 0
minute = 0
for line in c:
    time_len = re.match('(.*mins)', c)
    print(time_len)
    hour += int(time_len[1:2])
    minute += int(time_len[4:5])
print(hour + ' ' + minute)
    
    