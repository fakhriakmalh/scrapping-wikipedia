# importing the libraries
from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

# mendapatkan html dari url
url = "https://en.wikipedia.org/wiki/Provinces_of_Indonesia"
html_content = requests.get(url).text
soup = BeautifulSoup(html_content, "lxml")

#mendapatkan html keseluruhan tabel
table_province = soup.find("table",attrs={"class":"wikitable"})
#mendapatkan data dari tabel
data_table_province = table_province.tbody.find_all("tr")
#mendapatkan heading dari tabel
heading = [i.text.replace('\n','').replace('Numberof','Number of').replace('ofr','of r') for i in data_table_province[0].find_all('th')]
heading.remove('Arms')

#data provinsi
provinsi , indonesia_acronym, ISO, Capital, Population_2015, Area_km2, Population_density, Geographical_unit, kota_kab, kota, kab = [],[],[],[],[],[],[],[],[],[],[]
for num in range(1,len(data_table_province)) : 
  provinsi.append(data_table_province[num].find_all('td')[1].text)
  indonesia_acronym.append(data_table_province[num].find_all('td')[2].text)
  ISO.append(data_table_province[num].find_all('td')[3].text)
  Capital.append(data_table_province[num].find_all('td')[4].text)
  Population_2015.append(data_table_province[num].find_all('td')[5].text)
  Area_km2.append(data_table_province[num].find_all('td')[6].text)
  Population_density.append(data_table_province[num].find_all('td')[7].text)
  Geographical_unit.append(data_table_province[num].find_all('td')[8].text)
  kota_kab.append(data_table_province[num].find_all('td')[9].text)
  kota.append(data_table_province[num].find_all('td')[10].text)
  kab.append(data_table_province[num].find_all('td')[11].text.replace('\n',''))

#create dataframe
df = pd.DataFrame(list(zip(provinsi , indonesia_acronym, ISO, Capital, Population_2015, Area_km2, Population_density, Geographical_unit, kota_kab, kota, kab)), 
               columns = heading) 
