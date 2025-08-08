from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello from Jenkins-built Dockerized Flask app!<br> I'm Nanditha, This is my assignment crertaed for Better."
