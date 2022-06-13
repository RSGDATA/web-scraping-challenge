from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from pymongo import DESCENDING
import scrape_mars  # from scrape_mars import *

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars")



# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # scrape mars data
    mars_data = {
        "image": scrape_mars.scrape_scan_image(),
        "title": scrape_mars.scrape_mars_title(),
        "paragraph": scrape_mars.scrape_mars_para()
    }

    # Insert mars data into mongodb
    collection = mongo.db["scrapedata"]
    collection.insert_one(mars_data)

    # Redirect back to home page
    return redirect("/")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    collection = mongo.db["scrapedata"]
    mars_data = collection.find_one(sort=[('_id', DESCENDING)])

    # if no data in mongo, scrape/insert some into mongo
    if mars_data==None:
        return redirect("/scrape")

    # Return template and data
    return render_template("index.html",
        image_link = mars_data["image"],
        mars_title = mars_data["title"],
        mars_para = mars_data["paragraph"]
    )






if __name__ == "__main__":
    app.run(debug=True)