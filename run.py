import os
# os is from the python standard library.
# to add some extra functionality that Flask does not contain

os.environ.setdefault("secret_key", "some_secret")
# This may go under import statements
# enter the this data on the Key config in heroku

# json to get data from the
# file data/company.json
import json

from flask import Flask, render_template, request, flash
# the capital letter
# indicate that Flask is a class
# request: it will handle methods (post get)
# Flash messages for users. Needs ...
# ...to crete secret key Under app = Flask(...)

# we need to create an
# instance of a Flask before we get started.
# See below line
# __name__ is a built in variable from
#  python used when there is only one module/app/appname
app = Flask(__name__)
# app.secret_key = "some_secret"
# I think this is the unsafe way to place the secret key
#  the other way to show the secret key blow import line on top.



# we use the route decorator
# A decorator is a way
#  to wrap functions
# (route decorator: route()
# a decorator starts with @ sign
# (AKA py notation))
# to tell Flask what URL should trigger the function


@app.route("/")
def index():  # index view
    return render_template("index.html")
# return "<h1>Hello, </h1><h2>World</h2>"
# you can render html from python file.
# a better way is use the template. See below
# end of index view


@app.route("/about")
def about():  # about view
    # piece of code that is meant to work with Json
    data = []
    with open("data/company.json", "r") as json_data:
        # json_data is how we are
        # going to refer to "data/company.json"
        data = json.load(json_data)
    # end of piece of code for json
    return render_template("about.html", page_title="About", company=data)


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}

    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj['url'] == member_name:
                member = obj
    return render_template("member.html", member=member)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
            request.form["name"]))
        # print(request.form)
        # request.form return the values from input, based on name=""
    return render_template("contact.html", page_title="Contact")


@app.route("/career")
def career():
    return render_template("career.html", page_title="Career")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
    # oque eh __main__? Eh o name do default module in python
    # oque eh e o faz run()?
    # it run the app with the
    # arguments between parentesis
    # oque eh port?
    # O que eh host?
    # o que eh debug?
    # IMPORTANT, this can only be set
    # to true when you are in
    # development environment.
    # To use it in production will be
    # a security flaw.
    # Meaning of debug=true :
    # Allow troubleshooting capabilities
