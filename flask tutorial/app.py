from flask import Blueprint, render_template, request, jsonify, redirect, url_for
                            #for html template import

views = Blueprint(__name__,"views") # blueprint is like a mini app inside the main app. It helps organize the code by grouping related routes

@views.route("/") # maps the root url(/) to the home function
def home():
    # return "home page"
    return render_template("index.html", name="Jawaher")

"""@views.route("/profile/<username>")
def profile(username):
    return render_template("index.html", name = username)"""

"""@views.route("/profile")
def profile():
    args = request.args # gets all the query parameters from the URL
    name = args.get('name') #Extracts the value of the name parameter
    return render_template("index.html", name = name)"""

@views.route("/profile")
def profile():
    return render_template("profile.html")


@views.route("/json") #maps the /json Url to get_json function
def get_json():
    return jsonify({'name': 'Jawaher Smari', 'flask coolness': '100%'}) #using python code, make it in json's format

@views.route("/data")
def get_data():
    data = request.json #extracts json data sent in the request body (from a POST request)
    return jsonify(data) #sends back the same json data as a response

@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("app.get_json"))