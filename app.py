from flask import Flask, render_template, request

import iris_prediction
import json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def predict_iris():

    data = request.form.to_dict()
    # print(data)

    to_predict = [[float(data[key]) for key in data.keys()]]
    # print(f"to predict: {to_predict}")

    pred_result = iris_prediction.predict(to_predict)
    # return str(pred_result) if len(pred_result) != 0 else 'erreur'
    return pred_result

@app.route('/', methods=['GET'])
def home():
    return render_template('hello.html')


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)