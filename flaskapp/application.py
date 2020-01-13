from flask import Flask
from pymongo import MongoClient
application = app = Flask(__name__)

# Connect to MongoDB
client =  MongoClient("")
db = client['city-data']
collection = db['Census-Data']


def querydata(city_state):
    """
    Note: will query base on id rather than state and city name
    """
    state = city_state.split
    myquery = {"State": state} #TODO add query by state & city 
    docs = collection.find(myquery)
    data = []
    for x in docs:
        data.append(x)
    return str(data)


# Dynamic End Point
@app.route("/<city_state>")
def hello(city_state):
    
    # TODO Make calls to mongoDB to retrieve city data

    # TODO return city data
    return(querydata(city_state))

if __name__ == "__main__":
    app.run()


