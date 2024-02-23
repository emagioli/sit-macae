## Python code to retrieve data from SIT MACAÉ BUS TIMETABLE

from bs4 import BeautifulSoup
import csv
import requests

link = 'https://docs.google.com/spreadsheets/d/11ivzntv3Sa7REMnzG74ItI2SE0nZ8u6V/edit#gid=1489261462'

html = requests.get(link).text
soup = BeautifulSoup(html, 'lxml')
tables = soup.find_all('table')
print(tables)

index = 0

for table in tables:
    with open('tabela_'+str(index)+'.csv','w',encoding='utf8') as f:
        wr = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC, lineterminator='\n')
        wr.writerows([[td.text for td in row.find_all("td")] for row in table.find_all("tr")])
    index += 1