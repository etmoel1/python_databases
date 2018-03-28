
# python_databases
Code Louisville Python for Databases

Hello,

This is my modest attempt at a project which should fulfill all the requirements for the Code Louisville Python 
for Databases course. It is not overly complicated, and does not really answer any questions of much substance,
but I believe it proves the concept of being able to build the project with all the requirements, and will help me
towards being able to build bigger things moving forward. Albeit this course was difficult, I learned a lot, and look
forward to building projects and writing code that I am proud of, and continuing to learn!

This simple project takes a dataset from louisville.gov (a CSV file) which contains all criminal data collected
from the year 2016. I run a script that pulls the data, then run a script to delete several unnecessary columns
of data that I did not need or was not necessary to any of the analysis that I was considering undertaking.

I take the scrubbed data and load it into a SQLite3 database, where I filter out results for 3 different zip codes
in the area. I take a count of the number of incidents for each zip code, and load it into a bokeh bar chart which
is visualized via html. This bar chart illustrates the stark difference of crime incidents for 2016 betwen the zip codes 
specified.

Please see the requirements.txt file for special modules needed to run this script. It includes

requests
bokeh
sqlite3
pandas
csv
