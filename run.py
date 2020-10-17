import os
# os is from the python standard library. 
# to add some extra functionality that Flask does not contain

from flask import Flask, render_template
# the capital letter 
# indicate that Flask is a class

# we need to create an instance of a Flask before we get started.
* See below line
app = Flask(__name__) # __name__ is a built in variable from python used when there is only one module/app/appname

# we use the route decorator
# A decorator is a way to wrap functions
# (route decorator: route(), 
# a decorator starts with @ sign(AKA py notation)) 
# to tell Flask what URL should trigger the function
@app.route("/")
def index(): # index view
    return render_template("index.html")
 # return "<h1>Hello, </h1><h2>World</h2>" you can render html from python file. 
    #a better way is use the template. See below
# end of index view

@app.route("/about")
def about():# about view
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)
    # oque eh __main__? Eh o name do default module in python
    # oque eh e o faz run()? it run the app with the arguments between parentesis
    # oque eh port? 
    # O que eh host?
    # o que eh debug? IMPORTANT, this can only be set to true when you are in development environment. To use it in production will be a security flaw. Meaning of debug=true : Allow troubleshooting capabilities
