from flask import Flask, render_template
import populartimes

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/<placeid>", methods=["GET"])
def getPlaces(placeid):
    return populartimes.get_id("API_KEY", placeid)

if __name__ == "__main__":
    app.run(host='0.0.0.0',  port=80)
