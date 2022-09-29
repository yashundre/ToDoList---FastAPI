
from urllib import response
import pymongo

mongoURI = "mongodb://localhost:27017"
client = pymongo.MongoClient(mongoURI)

db = client["TODO"]
collection = db["todo"]

def create(data):
    data = dict(data)
    response = collection.insert_one(data)
    return str(response.inserted_id)


def all():
    response = collection.find({},{"_id":0,"task":1,"description":1})
    data = []
    for i in response:
        # i["_id"] = str(i["_id"]) 
        data.append(i)
    return data
    

def get_one(condition):
    response = collection.find_one({"task":condition})
    response["_id"] = str(response["_id"])
    return response

def update(data):
    data = dict(data)
    response = collection.update_one({"task":data["task"]},{"$set":{"description":data["description"]}})
    return response.modified_count

def delete(name):
    response = collection.delete_one({"task":name})
    return response.deleted_count



