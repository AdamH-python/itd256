import pymongo
from pymongo import MongoClient

def query(x):
    global mycol
    mydoc = mycol.find(x)
    for x in mydoc:
        print(x)
    
# Connecting to database and collections
client = MongoClient("mongodb+srv://adamghellinga:8hweCqVsMeW1uEzE@learningmongodb.0nigmus.mongodb.net/?retryWrites=true&w=majority&appName=LearningMongoDB")
mydb = client["mydatabase"]
mycol = mydb["customers"]

# Adding data to the collection.
mydict = { "name": "John", "address": "Highway 37" }
x = mycol.insert_one(mydict)
print(x.inserted_id)


### Checking if database is made, it is not created until data is entered into it.
print(' ')
print(client.list_database_names())
# OR DO
dblist = client.list_database_names()
if "mydatabase" in dblist:
    print("The database exists.")



### Checking if collection made, like the database is not created until data is entered.
print(' ')
print(mydb.list_collection_names())
# OR DO 
collist = mydb.list_collection_names()
if "customers" in collist:
    print("The collection exists.")



myquery = {"address": "Highway 37"}

mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)
    

# Gets VERY strange in queries

myquery = { "address": { "$gt": "F" } }

query(myquery)

# For exact matches

myquery = { "address": { "$regex": "^S" } }

query(myquery)
    

# Sorting (Descending), default is ascending
mydoc = mycol.find(myquery).sort("Address", -1)

for x in mydoc:
    print(x)
    
# Use .delete_one with a query to delete the first entry matches
# Use .delete_many to get rid of everything under a query
# Use .drop to delete a collection


newvalues = { "$set": { "address": "Canyon 123" } }
mycol.update_one(myquery, newvalues)

# .limit() works as expected