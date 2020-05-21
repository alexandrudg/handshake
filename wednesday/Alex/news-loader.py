import csv
import json
import requests
import yaml

#import general settings
config = yaml.safe_load(open("config.yaml"))
settings = config['news_locations']

#Get today's date for file naming
from datetime import datetime
now = datetime.now()

for setting in settings:
  # Request news and encoding
  url = "https://newsapi.org/v2/top-headlines?" + setting["query"] + "&apiKey=" + setting["news_key"]
  r = requests.get(url=url)
  text = r.text
  parsed = json.loads(text)
  articles = parsed['articles']
  csv_file = setting["filename"] + "_" + now.strftime("%Y%m%d") + ".csv"

  try:
    with open(csv_file, 'w') as csvfile:

      # Prepare writer and file header
      writer = csv.DictWriter(csvfile, fieldnames=setting['fields'], extrasaction='ignore', delimiter=';')
      writer.writeheader()

      # Write articles to CSV file
      for article in articles:
        writer.writerow({
          "source_id": article['source']['id'],
          "source_name": article['source']['name'],
          "author": article['author'],
          "title": article['title'],
          "description": article['description'],
          "url": article['url'],
          "url_to_image": article['urlToImage'],
          "published_at": article['publishedAt'],
          "content": article['content']
        })
  except IOError:
    print("I/O error")
