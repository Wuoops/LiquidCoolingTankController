import pymongo

MongoAddr = "mongodb://localhost:27017/"
Dbname = "LcpDataBase"
conn = pymongo.MongoClient(MongoAddr)
db = conn[Dbname]
col = db['Node1']
x = col.find({},{'_id':0})
for i in x :
    print(i)

print(x)