# main.py
from flask import Flask, render_template
from utils import fetch_trail_data, process_trail_data

app = Flask(__name__)

@app.route("/")
def index():
    raw_data = fetch_trail_data()
    trails = process_trail_data(raw_data)
    return render_template("index.html", trails=trails)

@app.route("/map")
def map_view():
    raw_data = fetch_trail_data()
    trails = process_trail_data(raw_data)
    return render_template("trail_map.html", trails=trails)

if __name__ == "__main__":
    app.run(debug=True)
