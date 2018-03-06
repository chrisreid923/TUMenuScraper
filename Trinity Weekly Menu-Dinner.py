
# coding: utf-8

# In[4]:


#Weekly Dinner Menu
from bs4 import BeautifulSoup
import requests
import pandas as pd

page = requests.get("https://trinity.campusdish.com/Commerce/Catalog/Menus.aspx?LocationId=1031&PeriodId=1473&MenuDate=&Mode=week")
soup = BeautifulSoup(page.text, 'lxml')

menu = soup.find_all('div',{'class':'menu-details-day'})

d = []

for day in menu:
    day_of_week = day.find('h2').text
    stations = day.find_all('div',{'class':'menu-details-station'})

    for station in stations:
        station_type = station.find('h4').text
        foods = station.find_all('div',{'class': 'menu-details-station-item'})
        for food in foods:
            item = food.find('div',{'class':'menu-name'}).text.replace('\n','')
            d.append((day_of_week,station_type,item))

df = pd.DataFrame(d,columns=('Day','Menu','Food'))
print(df)


# In[5]:


df.to_csv("C:/Users/bombo/Desktop/TU_Din.csv")

