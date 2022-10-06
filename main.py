
import pymongo
# mongodb atlas url
uri = "mongodb://pym:pym@ac-fbpllsj-shard-00-00.fn5hurg.mongodb.net:27017,ac-fbpllsj-shard-00-01.fn5hurg.mongodb.net:27017,ac-fbpllsj-shard-00-02.fn5hurg.mongodb.net:27017/?ssl=true&replicaSet=atlas-hliigi-shard-0&authSource=admin&retryWrites=true&w=majority"

# connect mongo db with cloud
myclient = pymongo.MongoClient(uri)
if (myclient):
  print("Connected")
else:
  print("Not connected")
  
#  database❤✌
  #  create database
mydb = myclient["createdDb"]
#  get all database
dblist = myclient.list_database_names()
print(dblist)
if "pymango" in dblist:
  print("The database exists.")
else:
  print(" database does not exist ")

  #  collection😊
  # create collection
col = mydb["cretedCol"]  
col2 = mydb["InsertMulWith"]  
col3 = mydb["InsertMulWithId"]  
#  get all collections
collist = mydb.list_collection_names()
print(collist)
if "cretedCol" in collist:
  print("The collection exists.")
else:
  print("The collection   does not exists.")

  
  #  Document 😁
mydict = { "name": "John", "address": "Highway 37" }
#  insert one document 
x = col.insert_one(mydict)
print(x.inserted_id)

#  insert multiple document 
mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]
x = col2.insert_many(mylist)
#print list of the _id values of the inserted documents:
print(x.inserted_ids)
#  insert multiple document with id
# mylist3 = [
#   { "_id": 1, "name": "John", "address": "Highway 37"},
#   { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
#   { "_id": 3, "name": "Amy", "address": "Apple st 652"},
#   { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
#   { "_id": 5, "name": "Michael", "address": "Valley 345"},
#   { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
#   { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
#   { "_id": 8, "name": "Richard", "address": "Sky st 331"},
#   { "_id": 9, "name": "Susan", "address": "One way 98"},
#   { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
#   { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
#   { "_id": 12, "name": "William", "address": "Central st 954"},
#   { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
#   { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
# ]

# x = col3.insert_many(mylist3)

#print list of the _id values of the inserted documents:
print(x.inserted_ids)

# find document 😉

#  find one 
col2Data = col2.find_one()
print(col2Data)
col3Data = col3.find_one()
print(col3Data)

# find all😉
col2DataMul = col2.find()
for x in col2DataMul:
  print(x)
print(col2DataMul)
col3DataMul = col3.find()
print(col3DataMul)
for x in col3DataMul:
  print(x)
# Return Only Some Fields
  print("Return Only Some Fields")
  #  1 for include and 0 for exclude
  for x in col2.find({},{"_id":0,  "name": 1, "address": 1 }):
    print(x)

