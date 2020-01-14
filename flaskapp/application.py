from flask import Flask, jsonify
from decouple import config
from flask_pymongo import PyMongo


application = app = Flask(__name__)

# Connect to MongoDB

app.config['MONGO_URI'] = config('MONGO_URI')
mongo = PyMongo(app)
ACCESS_KEY = config('ACCESS_KEY')

# Dynamic End Point
@app.route(f"/")
def home():

  return 'hello'


@app.route(f"/{ACCESS_KEY}/citydata/<num>")
def hello(num):
  doc = mongo.db.alldata.find_one({'_id':int(num)})
  return jsonify(doc)


if __name__ == "__main__":
    app.run(debug=True)
