import csv
import pytz
from datetime import datetime
from links import MainPage


class WebScraper:
    def __init__(self) -> None:
        self.url = "https://www.theverge.com"

    def getArticleLinks(self):
        main_page = MainPage()
        link_list = main_page.getArticleLinkList(self.url)
        return link_list
    
    def makeCSVFile(self):
        today = datetime.today().strftime('%d%m%Y')
        filename = today + '_verge.csv'
        return filename

    def convertToIndianTimeZone(self, datetime_str):
        datetime_obj = datetime.fromisoformat(datetime_str[:-5])
        indian_timezone = pytz.timezone('Asia/Kolkata')
        datetime_obj = datetime_obj.astimezone(indian_timezone)
        date = datetime_obj.strftime('%d-%m-%Y')
        return date

    def writeToCSV(self):
        file = self.makeCSVFile()
        with open(file, mode='w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'URL', 'headline', 'author', 'date']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            # Get List of Links of Different Articles
            link_list = self.getArticleLinks()

            # Iterate Through Each Article and Write the details to CSV File
            for i,link in enumerate(link_list):
                # Get Soup of each Article
                main_page = MainPage()
                link = self.url + link
                articles = main_page.getArticleSoup(link)

                # Now obtain the required details and write it to CSV File
                for article in articles:
                    headline = article.head.title.text.strip()
                    url = article.head.find('link',{"rel":"canonical"})['href']
                    author = article.body.find('span', class_='font-medium uppercase tracking-6').a.text.strip()
                    datetime_str = article.body.find('time', class_='duet--article--timestamp font-polysans text-12')['datetime']

                    # Convert this Time to Indian Time Zone
                    date = self.convertToIndianTimeZone(datetime_str)

                    # write the information to the CSV file
                    writer.writerow({'id': i+1, 'URL': url, 'headline': headline, 'author': author, 'date': date})


scraper = WebScraper()
scraper.getArticleLinks()
scraper.writeToCSV()
