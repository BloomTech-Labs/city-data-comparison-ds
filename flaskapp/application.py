from flask import Flask
from pymongo import MongoClient
application = app = Flask(__name__)



# Connect to MongoDB
client =  MongoClient("")
db = client['city-data']
collection = db['Census-Data']


def querydata(city_state):

    state = city_state.split('-')[0]
    city = city_state.split('-')[1]
    myquery = {"State": state} #TODO add query by state & city 
    docs = collection.find(myquery)
    return docs


# Dynamic End Point
@app.route("/<city_state>")
def hello(city_state):
    
    # TODO Make calls to mongoDB to retrieve city data

    # TODO return city data
    return(city_state)

if __name__ == "__main__":
    app.run()


