import requests, json, csv

# For CSV naming structure cron
from datetime import datetime
now = datetime.now()

# Query string abd CSV file prefix
questions = [
  {
    "filename": "berlin_",
    "query": "q=berlin"
  },
  {
    "filename": "ios_",
    "query": "q=ios"
  },
  {
    "filename": "us_",
    "query": "country=us"
  }
]

# CSV data model
csv_columns = ["author", "title", "description", "url", "urlToImage", "publishedAt", "content"]

for question in questions:

  #Request news and encoding
  url = "https://newsapi.org/v2/top-headlines?" + question["query"] + "&apiKey=bff008e5505d4e3fa3b23d659c40ed6a"
  r = requests.get(url=url)
  text = r.text
  parsed = json.loads(text)
  articles = parsed['articles']
  csv_file = question["filename"] + now.strftime("%Y%m%d") + ".csv"

  try:
    with open(csv_file, 'w') as csvfile:

      #Prepare writer and file header
      writer = csv.DictWriter(csvfile, fieldnames=csv_columns, extrasaction='ignore', delimiter = ';')
      writer.writeheader()

      #Write articles to CSV file
      for article in articles:
        writer.writerow(article)

  except IOError:
      print("I/O error")
