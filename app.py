from flask import Flask, jsonify, render_template, url_for
import json


app = Flask(__name__)


with open("./data/collections.json", encoding="utf-8") as json_data_res:
    collections = json.load(json_data_res)


@app.route("/", methods=["GET"])
@app.route("/index-api", methods=["GET"])
@app.route("/mino-api", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/api/v.1.0/get-collections", methods=["GET"])
@app.route("/api/get-collections", methods=["GET"])
@app.route("/mino-api/get-collections", methods=["GET"])
def get_collections():
    return jsonify({ "collections": collections })


@app.route("/api/v.1.0/get-collections/<int:collection_id>", methods=["GET"])
@app.route("/api/get-collections/<int:collection_id>", methods=["GET"])
@app.route("/mino-api/v.1.0/get-collections/<int:collection_id>", methods=["GET"])
def get_collection(collection_id):
    return collections[collection_id]


if __name__ == "__main__": 
    app.run(debug=False)