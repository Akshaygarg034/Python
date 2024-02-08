# ************************  News App  ************************

import requests

def news(category):
    url = (f"https://newsapi.org/v2/everything?q={category}&apiKey=a83a6770c82940e981890f400db50ec8")
    response = requests.get(url)
    news = response.json()
    print("\n")
    for article in news["articles"]:
        print(article['title'])
        print(article['description'])
        print('---------------------------------------------------')

category = input("Enter the category of news you want to read: ")
news(category)
