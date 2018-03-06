
# coding: utf-8

# In[18]:


#Weekly Breakfast Menu
from bs4 import BeautifulSoup
import requests
import pandas as pd

#Loads the selected webpage with beautiful soup. BeautifulSoup can be used to parse webpages to get specifc information automatically.
page = requests.get("https://trinity.campusdish.com/Commerce/Catalog/Menus.aspx?LocationId=1031&PeriodId=1471&MenuDate=&Mode=week")
soup = BeautifulSoup(page.text, 'lxml')

menu = soup.find_all('div',{'class':'menu-details-day'}) #Finds the menu items that reside in menu-details-day.

d = []

for day in menu:
    day_of_week = day.find('h2').text #Finds day of week in h2 tag.
    stations = day.find_all('div',{'class':'menu-details-station'}) #Finds all stations.

    for station in stations:
        station_type = station.find('h4').text #Finds the type of station in the h4 tag.
        foods = station.find_all('div',{'class': 'menu-details-station-item'}) #Finds all food items inside the specified class.
        for food in foods:
            item = food.find('div',{'class':'menu-name'}).text.replace('\n','') #Finds the name of all food items with newlines replaced by space.
            d.append((day_of_week,station_type,item)) #Adds the items to the array

df = pd.DataFrame(d,columns=('Day','Menu','Food')) #Creates a dataframe using Pandas adding column names the previous array.
print(df) #Prints the dataframe to make sure it is working


# In[20]:


df.to_csv("C:/Users/bombo/Desktop/TU_Break.csv") #Converts the DF to a csv file for use in the menu app. 

