import numpy as np
import pandas as pd
from waitress import serve
from flask import Flask, request, jsonify
import pickle


app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route("/", methods=["GET", "POST"])
def bank_predict():
    data = {"success": False}
    params = request.args

    if "age" in params.keys():
        new_row = {"age": params.get("age"), "income": params.get("income"),
                   "family": params.get("family"), "ccavg": params.get("ccavg"),
                   "education": params.get("education"), "mortgage": params.get("mortgage"),
                   "securities": params.get("securities"), "cd": params.get("cd"),
                   "online": params.get("online"), "credit": params.get("credit")}
        new_x = pd.DataFrame.from_dict(new_row, orient="index").transpose()

        data["response"] = str(model.predict(new_x)[0])
        data["success"] = True
    return jsonify(data)




if __name__=="__main__":
    serve(app, host="0.0.0.0", port=5000)


