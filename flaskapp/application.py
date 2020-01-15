from flask import Flask, jsonify, request, render_template
from decouple import config
from flask_pymongo import PyMongo
from flask_cors import CORS
from city_spelling_matcher import spellchecker


application = app = Flask(__name__)

# Connect to MongoDB

app.config['MONGO_URI'] = config('MONGO_URI')
mongo = PyMongo(app)
ACCESS_KEY = config('ACCESS_KEY')
CORS(app)


# Dynamic End Point
@app.route(f"/")
def home():

    return render_template('start.html')


@app.route(f"/{ACCESS_KEY}/citydata/<num>")
def allcitydata(num):
  doc = mongo.db.alldata.find_one({'_id':int(num)})
  return jsonify(doc)

@app.route(f"/{ACCESS_KEY}/matchcity/<words>")
def spelling_matcher(words):
  doc = spellchecker(words)
  return jsonify(doc)



if __name__ == "__main__":
    app.run(debug=True)
