import requests
import pandas as pd
from bs4 import BeautifulSoup

data=[]

url = "https://books.toscrape.com/"
response= requests.get(url)


soup = BeautifulSoup(response.text,"html.parser")
cards=soup.find_all("article", class_="product_pod")

for card in cards:
    h3=card.find("h3")
    a_tag = h3.find("a")
    title = a_tag.get("title")
    raw_price=card.find("p" , class_="price_color").text
    price=raw_price.replace("£", "").replace("Â", "")
    data.append({
        "title":title,
        "price":price
    })
df=pd.DataFrame(data)
df.to_csv("books.csv", index=False)

print("Saved!")



