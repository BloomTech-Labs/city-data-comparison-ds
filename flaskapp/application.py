from flask import Flask, jsonify, request, render_template, redirect, url_for
from decouple import config
from flask_pymongo import PyMongo
from flask_cors import CORS
from city_spelling_matcher import *
from charts import *



application = app = Flask(__name__)

# Connect to MongoDB
app.config["JSON_SORT_KEYS"] = False
app.config['MONGO_URI'] = config('MONGO_URI')
mongo = PyMongo(app)
ACCESS_KEY = config('ACCESS_KEY')
CORS(app)



# Dynamic End Point
@app.route(f"/")
def home():
    return redirect(url_for('docs'))

@app.route(f"/docs")
def docs():
    seattledata = seattle()
    plot = housing(seattledata)
    return render_template('start.html', plot=plot)


@app.route(f"/{ACCESS_KEY}/citydata/<num>")
def allcitydata(num):
  doc = mongo.db.alldata.find_one({'_id':int(num)})
  return jsonify(doc)

@app.route(f"/{ACCESS_KEY}/matchcity/<words>")
def spelling_matcher(words):
    data = data_loader()
    doc = check_spelling(data, words)
    return jsonify(doc)



if __name__ == "__main__":
    app.run(debug=True)
