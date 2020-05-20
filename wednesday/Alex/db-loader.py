import sqlite3
import csv
import yaml

# import general settings
config = yaml.safe_load(open("config.yaml"))
settings = config['news_locations']

# Get today's date
from datetime import datetime

now = datetime.now()

for setting in settings:
  #Connect to sqlite & prepare table if it's not there
  qry = setting['sql_table_create']
  con = sqlite3.connect('toplines.sqlite')
  c = con.cursor()
  c.execute(qry)

  #Create secondary index
  createSecondaryIndex = "CREATE INDEX IF NOT EXISTS " + setting["secondary_index"] + " ON " + setting["table"] + "(" + setting["secondary_index"] + ")"
  c.execute(createSecondaryIndex)
  con.commit()
  c.close()

  con = sqlite3.connect('toplines.sqlite')
  cur = con.cursor()

  try:
    with open(setting["filename"] + "_" + now.strftime("%Y%m%d") + ".csv", 'rt',
              encoding='utf-8') as f:
      dr = csv.DictReader(f, delimiter=';')
      to_db = [(i['source_id'], i['source_name'], i['author'], i['title'], \
                i['description'], i['url'], i['url_to_image'], i['published_at'], i['content']) for i in dr]

    cur.executemany("INSERT INTO " + setting["table"] + " (source_id, source_name, author, title, description, url, \
      url_to_image, published_at, content) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
    con.commit()
    con.close()

  except IOError:
    print("I/O error")
