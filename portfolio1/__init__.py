import os
import uuid
from flask import Flask , render_template


app = Flask(__name__)

projects = [ 
    {
        "title" : "Habit tracker tracking app using python",
        "thumb" : "/habit-tracking.png",
        "hero" : "/habit-tracking-hero.png",
        "categories" : ["python","Flask"],
        "slug" : "habit-tracker",
        "production" : "https://www.udemy.com/course/web-developer-bootcamp-flask-python/learn/lecture/31495076#overview"
    },
     {
        "title" : "personal-finance tracking app using python",
        "thumb" : "/personal-finance.png",
        "hero" : "/personal-finance.png",
        "categories" : ["personal","finance"],
        "slug" : "habit-tracker",
    },
     {
        "title" : "Rest api tracking app using python",
        "thumb" : "/rest-api-docs.png",
        "hero" : "/rest-api-docs.png",
        "categories" : ["Rest","api"],
        "slug" : "habit-tracker",
    }
]


dwij = uuid.uuid4().hex
print(dwij)
@app.route("/")
def home():
    return render_template("home.html",projects=projects)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)