
from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/api/restaurants")
def restaurants():
    return jsonify(["Pizza Hut","Biryani Palace","Burger King"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
