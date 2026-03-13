import requests
from bs4 import BeautifulSoup

def search_news(query):
    url = f"https://news.google.com/rss/search?q={query}"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    items = soup.find_all("item")[:5]
    news = []
    for item in items:
        news.append(item.title.text)

    return news