import os
from os import path
if path.exists("env.py"):
    import env
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

# Linking my app to MongoDB
app.config["MONGO_DBNAME"] = 'reviewmanguezal'
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

# Creating a Instance for Pymongo
mongo = PyMongo(app)

@app.route("/manguezalclub")
def manguezalclub():
    return render_template('manguezalclub.html', manguezalclub=mongo.db.review.find())

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/addreview")
def addreview():
    return render_template("addreview.html", 
        categories=mongo.db.categories.find())

# This function will insert the data into mongodb accordingly and after that the user will be redirect to the page where they can see the review (Good practices")
@app.route("/insert_review", methods=['POST'])
def insert_review():
    review = mongo.db.review
    review.insert_one(request.form.to_dict())
    return redirect(url_for('manguezalclub'))

@app.route('/editreview/<review_id>')
def editreview(review_id):
    the_review = mongo.db.review.find_one({"_id": ObjectId(review_id)})
    all_categories = mongo.db.categories.find()
    return render_template('editreview.html', review = the_review, categories = all_categories)

@app.route('/update_review/<review_id>', methods=["POST"])
def update_review(review_id):
    review = mongo.db.review
    review.update({'_id': ObjectId(review_id)},
    {   
        'category_name' : request.form.get('category_name'),
        'name' : request.form.get('name'),
        'review' : request.form.get('review'),
        'date' : request.form.get('date')
        
    })
    return redirect(url_for('manguezalclub'))
@app.route('/deletereview/<review_id>')
def deletereview(review_id):
    mongo.db.review.remove({'_id': ObjectId(review_id)})
    return redirect(url_for('manguezalclub'))

@app.route('/get_categories')
def get_categories():
    return render_template('categories.html',
                           categories=mongo.db.categories.find())

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)