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
    mars_data = mongo.db.mars_data.find_one()
    return render_template('index.html', mars_data = mars_data)
# 
@app.route("/scrape")
def scraper():

    mars_data = mongo.db.mars_data
    mars_stuff = scrape_mars.scrape()
    mars_data.update({}, mars_stuff, upsert = True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)

return mars_data