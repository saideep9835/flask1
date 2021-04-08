import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello", methods=["GET","POST"])
def hello():
    if request.method == "GET":
        return "Please submit the form"
    else:
        name = request.form.get("name")
        return render_template("hello.html", name=name)
#@app.route("/more")
#def more():
#    return render_template("more.html")

#@app.route("/")
#def index():
 #   n = ["sai", "deep", "praneeth"]
 #   return render_template("index.html", n=n)
#@app.route("/")
#def index():
 #   now = datetime.datetime.now()
 #   new_year = now.month == 1 and now.day == 1
  #  new_year = True
  #  return render_template("index.html", new_year=new_year)
#@app.route("/bye")
#def bye():
    #headline = "Goodbye"
    #return render_template('index.html', headline=headline)
#@app.route("/<string:name>")
#def hello(name):
 #   name=name.upper()
  #  return f"<h1>Hello, {name}!</h1>"