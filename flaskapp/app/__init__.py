from flask import Flask, request, render_template, redirect, url_for
from decouple import config
from flask_pymongo import PyMongo
from flask_cors import CORS
from app.city_spelling_matcher import *
from app.charts import *
from flask import json
from flask import jsonify


def create_app():
    app = Flask(__name__, static_url_path='/app/static')

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
        plot = housingtest(seattledata)
        graphJSON = plot[0]
        ids = plot[1]
        content = plot[2]


        return render_template('start.html',
                               ids=ids,
                               graphJSON=graphJSON, content=content)


    @app.route(f"/{ACCESS_KEY}/citydata/<num>")
    def allcitydata(num):
      doc = mongo.db.alldata.find_one({'_id':int(num)})

      return jsonify(doc)

    @app.route(f"/{ACCESS_KEY}/matchcity/<words>")
    def spelling_matcher(words):
        data = data_loader()
        doc = check_spelling(data, words)
        return jsonify(doc)


    @app.route('/postjson', methods = ['POST'])
    def foo():
        data = request.get_json(force=True)
        return jsonify(data)

    return app
