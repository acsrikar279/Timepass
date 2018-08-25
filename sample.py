from pymongo import MongoClient
client = MongoClient()
print(client.database_names())
db = client.learning
print(db.collection_names())
c = db.resta.find({"borough":"Bronx"})

for i in c:
    print(i['cuisine'])