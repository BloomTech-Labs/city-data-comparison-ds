from pymongo import MongoClient
from decouple import config

MONGO_URI = config('MONGO_URI2')

client = MongoClient(MONGO_URI)

test  = client.SingleCity.yelp_data.find_one({"_id": "11527"})

print(test)
