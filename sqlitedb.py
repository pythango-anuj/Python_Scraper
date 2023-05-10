import sqlite3
import pandas as pd

conn = sqlite3.connect("articles_db")
c = conn.cursor()

#c.execute('''CREATE TABLE articles (id int, url text, headline text, author text, date date)''')

# load the data into a Pandas DataFrame
articles_data = pd.read_csv('14042023_verge.csv')

# write the data to a sqlite table
articles_data.to_sql('articles', conn, if_exists='append', index = False)

#Retrieve Data and print it to check
table = c.execute('''SELECT * FROM articles''')
print(table.fetchall())


