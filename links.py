import requests
from bs4 import BeautifulSoup


class MainPage:
    def __init__(self, features = None) -> None:
        pass

    # To obtain the List of Article links in TheVerge.com    
    def getArticleLinkList(self, url):
        # Send an HTTP request to the URL
        response = requests.get(url)

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'lxml')

        urls = []
        count=0
        orgi_index = [7,9,11,13,15,17]
        for url in soup.find_all('a'):
            if url.attrs['href'] not in urls:
                count+=1
                if count in orgi_index:
                    urls.append(url.attrs['href'])
        return urls
    
    # To obtain the soup of Ecah Article Page
    def getArticleSoup(self, url):
        # Send an HTTP request to the URL
        response = requests.get(url)

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'lxml')

        articles = soup.find_all('html')
        return articles
