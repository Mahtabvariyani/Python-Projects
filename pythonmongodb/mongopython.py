import pymongo
from pymongo import MongoClient
cluster = MongoClient("mongodb://localhost:27017")
db = cluster["test"]
collection = db["test"]


post1 = {"_id": 1, "name": "Geranesh" ,"last_name":"Ashoori", "score": 10}
post2 = {"_id": 2, "name": "Mahtab","last_name":"Variyani" ,"score": 2}

#collection.insert_many([post1,post2])

results = collection.find({"name":"Geranesh"})

#print(results)

for result in results:
    print(result["name"])
