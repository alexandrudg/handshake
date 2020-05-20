import sqlite3
import timeit
import yaml

# import general settings
config = yaml.safe_load(open("config.yaml"))
settings = config['news_locations']

# Connect to sqlite
con = sqlite3.connect('toplines.sqlite')
cur = con.cursor()
test = cur.execute(config['question1'])
stmt = lambda s: "cur.execute(config['"+s+"']).fetchall()"

#Time queries
q1 = timeit.timeit("stmt('question1')", 'from __main__ import cur, config, stmt', number=100000)
q1_index = timeit.timeit("stmt('question1-2')", 'from __main__ import cur, config, stmt', number=100000)
q2 = timeit.timeit("stmt('question2')", 'from __main__ import cur, config, stmt', number=100000)
q2_index = timeit.timeit("stmt('question2-2')", 'from __main__ import cur, config, stmt', number=100000)
q3 = timeit.timeit("stmt('question3')", 'from __main__ import cur, config, stmt', number=100000)
q3_index = timeit.timeit("stmt('question3-2')", 'from __main__ import cur, config, stmt', number=100000)

con.commit()
con.close()

print('Q1 no index:      ', q1)
print('Q1 with index:    ', q1_index)
print('Q2 no index:      ', q2)
print('Q2 with index:    ', q2_index)
print('Q3 no index:      ', q3)
print('Q3 with index:    ', q3_index)
