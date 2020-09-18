import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
from flask_pymongo import PyMongo
from splinter import Browser
from flask import Flask, render_template, redirect
import scrape_mars

####Begin flask app routes######
app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://localhost:27017/mars_db"
mongo = PyMongo(app)

@app.route("/")
def index():
    mars_data = mongo.db.mars_info_dict.find_one()
    return render_template('index.html', mars_data = mars_data)
# 
@app.route("/scrape")
def scrape():

    mars_data = mongo.db.mars_data
    mars_stuff = scrape_mars.scrape()
    mars_data.replace_one({}, mars_stuff, upsert = True)
    return ('Done Scraping! ')


if __name__ == "__main__":
    app.run(debug=True)

# return mars_data