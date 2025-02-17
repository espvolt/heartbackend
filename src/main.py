from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route("/uploadheartbeat", methods=["POST"])
def upload_heart_beat():
    if (request.is_json):
        data = request.get_json()

        print("received data: ", data)


        return "{\"response\": 200}", 200
    
if (__name__ == "__main__"):
    app.run(debug=True)