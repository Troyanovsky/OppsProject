from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == "GET":
        return ('''<!DOCTYPE html>
        <html>
        <body>
        <p>Click the button to get your coordinates.</p>

        <button onclick="getLocation()">Location</button>
        <p id="demo"></p>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>    <script>
        var x = document.getElementById("demo");

        function getLocation() {
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(showPosition);
            } else { 
                x.innerHTML = "Geolocation is not supported by this browser.";
            }
        }

        function showPosition(position) {
            x.innerHTML = "Latitude: " + position.coords.latitude + 
            "<br>Longitude: " + position.coords.longitude;
            var location = "Latitude: " + position.coords.latitude + 
            "\tLongitude: " + position.coords.longitude;
            $.ajax({
            type: 'POST',
            url: '/',
            data: JSON.stringify({"loc": location}),
            contentType: 'application/json;charset=UTF-8'
            });
            console.log(location);
        }
        </script>
        </body>
        </html>''')
    else:
        userLocation = request.get_json(force= True)
        print(userLocation["loc"])

if __name__ == '__main__':
    app.run(host='0.0.0.0')