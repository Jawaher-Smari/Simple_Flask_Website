from flask import Flask
from app import views

app = Flask(__name__)# initializing flask app

"""@app.route("/") #flask recognizes the URL because of @app.route
def home(): # flask calls the home function
    return "this is the home page" # flask sends this as the HTTP response"""

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/views") #access all the roots in the page views


if __name__ == '__main__':
    app.run(debug=True)# to run flask website
    # we can add ,port=8000 next to True so we specify the port where the website will be live



# So app.route is a decorator thats tells flask to link the home page(/) to the function below