import requests
from bs4 import BeautifulSoup
import mysql.connector
import json
import os

def parser():
    url = "https://inshorts.com/en/read/"
    
    #Get the inshort url
    response = requests.get(url)
    #Fetch the content from the response
    soup = BeautifulSoup(response.content, "html.parser")
    #Find all the headlines
    headlines = soup.find_all('span', {'itemprop': 'headline'})
    headlines_tuple = tuple()
    len(headlines)
    for i in range(len(headlines)):
        headlines_tuple = headlines[i].get_text()
    print(headlines_tuple)

# Saving in csv
# data = pd.DataFrame(headlines)
# data.to_csv("/Users/ajita/code/webscrapper/headlines.csv", index= True)

# Saving data to MySQL
    db = mysql.connector.connect(user=os.environ.get(
        'user'), password=os.environ.get('password'), database="your_database_name")
    cursor = db.cursor()
    add_news = ("INSERT INTO scraper_table"
                "(headlines_column) "
                "VALUES (%s)")
    data_news = headlines_tuple
    cursor.execute(add_news, (data_news,))
    db.commit()
    cursor.close()
    db.close()
