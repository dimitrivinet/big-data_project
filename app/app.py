from flask import Flask, render_template, request
from pymongo import MongoClient

import iris_prediction
import os

app = Flask(__name__)

# MONGO_ADDR = os.getenv('MONGO_ADDR', "localhost")
client = MongoClient("mongodb.default.svc.cluster.local", 27017)

db = client["toy_server_logs"]

logs = db["logs"]

@app.route('/', methods=['POST'])
def predict_iris():

    data = request.form.to_dict()
    # print(data)
    to_predict = [[float(data[key]) for key in data.keys()]]
    # print(f"to predict: {to_predict}")
    pred_result = iris_prediction.predict(to_predict)
    # return str(pred_result) if len(pred_result) != 0 else 'erreur'

    log = {"client": request.remote_addr, 
            "sep_len": data["sep_len"], 
            "sep_width": data["sep_width"], 
            "pet_len": data["pet_len"], 
            "pet_width": data["pet_width"], 
            "result": pred_result}

    # print(log)

    logs.insert_one(log)

    return pred_result

@app.route('/', methods=['GET'])
def home():
    return render_template('hello.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)