from tinydb import TinyDB, where
from datetime import datetime

db = TinyDB('./testDB.json')
db.insert({
        'Name' : 'Paul',
        'Age' : 1337,
        'DateTime' : datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })
db.insert({
        'Name' : 'Peter',
        'Age' : 42,
        'DateTime' : datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })

key = 'Age'
result = db.search((where(key) == 42) | (where(key) == 1337))
numberOfResults = 0
for item in result:
        numberOfResults += 1
        print item
print 'Found ' +  str(numberOfResults) + ' results.'


