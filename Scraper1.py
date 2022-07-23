#Import libraries
import requests
from bs4 import BeautifulSoup

#Requesting data 
req = requests.get("https://www.geeksforgeeks.org/")
#Create instance
soup = BeautifulSoup(req.content, "html.parser")

#Displaying website in html format
print(soup.prettify())

#Displaying title of website in html format
res = soup.title
print(res.prettify())

#Displaying title of website in text format
print(res.get_text())
