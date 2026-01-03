import requests
import pandas as pd
from bs4 import BeautifulSoup

data = []
url = "https://books.toscrape.com/"

while True:

    print("Scraping:", url)

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    cards = soup.find_all("article", class_="product_pod")

    for card in cards:
        title = card.find("h3").find("a").get("title")
        raw_price = card.find("p", class_="price_color").text
        price = raw_price.replace("£","").replace("Â","")

        data.append({
            "title": title,
            "price": price
        })

    nxt_btn = soup.find("li", class_="next")

    if not nxt_btn:
        break

    next_link = nxt_btn.find("a")["href"]

    if "catalogue" not in url:
        url = "https://books.toscrape.com/" + next_link
    else:
        url = "https://books.toscrape.com/catalogue/" + next_link

        print(len(data))
df=pd.DataFrame(data)
df.to_csv("books_all_pages.csv", index=False)
print("saved")
