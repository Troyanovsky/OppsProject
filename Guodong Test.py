from flask import Flask, render_template
from flask import request

app = Flask(__name__)
locations = []


@app.route('/')
def home():
    return (render_template("index.html"))

@app.route('/mapview', methods = ["GET","POST"])
def mapview():
    if request.method == "GET":
        return (render_template("mapview.html"))
    else:
        userLocation = (request.get_json(force= True)["ip"],
            request.get_json(force= True)["latitude"],
            request.get_json(force= True)["longitude"])
        locations.append(userLocation)
        print(locations)

@app.route('/result')
def result():
    return """

"""


if __name__ == '__main__':
    app.run(host='0.0.0.0')