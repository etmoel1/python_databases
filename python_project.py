import sqlite3
import requests
import csv
import pandas as pd
from bokeh.io import show, output_file
from bokeh.plotting import figure


#get request CSV dataset from louisville.gov

url = 'https://data.louisvilleky.gov/sites/default/files/Crime_Data_2016_0.csv'


with requests.Session() as s:
    download = s.get(url)
    decoded_content = download.content.decode('utf-8')
    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)


#manipulate data requirement, remove several columns not necessary for analysis

headers = my_list[0]
data = my_list[1:]
df = pd.DataFrame(data, columns=headers)
df.head()
df = df.drop(['INCIDENT_NUMBER', 'UOR_DESC', 'NIBRS_CODE', 'UCR_HIERARCHY', 'ATT_COMP','LMPD_DIVISION','LMPD_BEAT','ID'], axis=1)
df.head()


#connect and create sqlite3 database, loading DataFrame from above

conn = sqlite3.connect('louisville_crimes.db')
c = conn.cursor()
df.to_sql("louisville_crimes", conn, if_exists="replace")

#fetch and filter specific data using sql queries

c.execute("SELECT COUNT(date_reported) FROM louisville_crimes WHERE zip_code = 40217")
data_one = c.fetchall()
c.execute("SELECT COUNT(date_reported) FROM louisville_crimes WHERE zip_code = 40222")
data_two = c.fetchall()
c.execute("SELECT COUNT(date_reported) FROM louisville_crimes WHERE zip_code = 40212")
data_three = c.fetchall()

#bokeh code for visulation requirement -- bar chart

output_file("bars.html")

zips = ['Germantown/Highlands - 40217', 'Part of the East End - 40222', 'Shawnee/Portland/Parkland - 40212']

p = figure(x_range=zips, plot_height=425, title="2016 Crimes by Zip Code")
p.vbar(x=zips, top=[data_one[0], data_two[0], data_three[0]], width=0.8)

p.xgrid.grid_line_color = None
p.y_range.start = 500

show(p)