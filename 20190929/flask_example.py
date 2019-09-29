from flask import Flask

app = Flask(__name__)
@app.route("/")
def hello():
    return "<h1>Hello World</h1>"



# cmd> set FLASK_APP=flask_example.py
# cmd> flask run