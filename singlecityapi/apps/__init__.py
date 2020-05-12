from flask import Flask, request, render_template, redirect, url_for, jsonify
from decouple import config
from flask_pymongo import PyMongo
from flask_cors import CORS


def create_app():
    app = Flask(__name__, static_url_path='/apps/static')

    ACCESS_KEY = config('ACCESS_KEY')

    app.config["JSON_SORT_KEYS"] = False
    app.config['MONGO_URI'] = config('MONGO_URI')
    mongo = PyMongo(app)

    DB = mongo.db.client.get_database('SingleCity')
    CORS(app)

    @app.route(f"/")
    def home():
        return redirect('https://api.citrics.io/docs')

    @app.route(f"/{ACCESS_KEY}/singlecityWiki/<num>")
    def singlecityWiki(num):
        doc = DB.WikiReal.find_one({'_id': int(num)})
        return jsonify(doc)

    @app.route(f"/{ACCESS_KEY}/wikisum/<num>")
    def wikisum(num):
        doc = DB.wikidata.find_one({'_id': int(num)})
        return jsonify(doc)

    @app.route(f"/{ACCESS_KEY}/singlecityYelp/<num>")
    def singlecityYelp(num):
        doc = DB.yelp_data.find_one({'_id': str(num)})
        return jsonify(doc)

    @app.route(f"/{ACCESS_KEY}/statecrime/<sa>")
    def statecrime(sa):
        doc = DB.statecrime.find_one({'_id': str(sa).upper()})
        return jsonify(doc)
    return app