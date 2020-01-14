from flask import Flask
from flask import jsonify as json 
from pymongo import MongoClient
application = app = Flask(__name__)

# Connect to MongoDB
client =  MongoClient("mongodb+srv://citricuser:mattlukescott1@cluster0-f4vji.mongodb.net/test?retryWrites=true&w=majority")
db = client['citydata']
collection = db['alldata']


def querydata(id):
    """
    Query for the id and formats the query
    """
    
    myquery = {"_id": int(id)}
    docs = collection.find_one(myquery)

    return docs


# Dynamic End Point
@app.route("/<id>")
def hello(id):

    result = querydata(id)
    return json(result)

if __name__ == "__main__":
    app.run()


