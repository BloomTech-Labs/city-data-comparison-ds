from flask import Flask
from pymongo import MongoClient
application = app = Flask(__name__)

# Connect to MongoDB
client =  MongoClient("")
db = client['city-data']
collection = db['alldata']


def querydata(_id):
    """
    Query for the id and formats the query
    """
    state = city_state.split
    myquery = {"_id": state}
    docs = collection.find_one(myquery)
    return str(docs)


# Dynamic End Point
@app.route("/<_id>")
def hello(city_state):
    
    # TODO Make calls to mongoDB to retrieve city data

    # TODO return city data
    return(querydata(_id))

if __name__ == "__main__":
    app.run()


