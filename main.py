import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

website = 'https://www.worldometers.info/coronavirus/#countries'
website_url = requests.get(website).text
soup = BeautifulSoup(website_url, 'html.parser')

my_table = soup.find('tbody')

table_data = []

for row in my_table.findAll('tr'):
    row_data = []

    for cell in row.findAll('td'):
        row_data.append(cell.text)

    if (len(row_data) > 0):
        data_item = {"Country": row_data[0],
                     "TotalCases": row_data[1],
                     "NewCases": row_data[2],
                     "TotalDeaths": row_data[3],
                     "NewDeaths": row_data[4],
                     "TotalRecovered": row_data[5],
                     "ActiveCases": row_data[6],
                     "CriticalCases": row_data[7],
                     "Totcase1M": row_data[8],
                     "Totdeath1M": row_data[9],
                     "TotalTests": row_data[10],
                     "Tottest1M": row_data[11],
                     }
        table_data.append(data_item)

df = pd.DataFrame(table_data)

df.to_excel('Covid19_data.xlsx', index=True)
# df.to_csv('Covid19_data.csv', index=True)
# df.to_html('Covid19_data.html', index=True)
