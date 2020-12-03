import sqlite3
import requests
from bs4 import BeautifulSoup
from datetime import datetime

conn = None
conn = sqlite3.connect("db/db_scrapper.db")     

def showAll():         
    cur = conn.cursor()    
    cur.execute("SELECT * FROM LOG_TEST")
    rows = cur.fetchall()
    for row in rows:
        print(row)   
        
def returnLast():
    cur = conn.cursor()    
    cur.execute("SELECT count(*) + 1 FROM LOG_TEST")
    row = cur.fetchall()
    return row       
        
def insertRow(val1):
    dateTimeObj = datetime.now()
    cur = conn.cursor()
    query = 'INSERT INTO LOG_TEST(LOG_TEXT,LOG_DATE) VALUES (?, ?)'
    cur.execute(query,(val1,dateTimeObj))
    conn.commit()
    return cur.lastrowid   

def rqsts():
    URL = 'https://serieslan.com/las-aventuras-de-tom-sawyer'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content,'html.parser')
    print(soup)
    

        
if __name__ == "__main__":  
    rqsts() 
"""     getlast = insertRow("R1000")
    print(getlast)
    showAll() """

    
    
    
    




