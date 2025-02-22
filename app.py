from flask import Flask,request, url_for, redirect, render_template, jsonify
from pycaret.regression import setup, create_model,plot_model,save_model, load_model, predict_model
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

model = load_model('deployment_28042020')
cols = ['age', 'sex', 'bmi', 'children', 'smoker', 'region']

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [x for x in request.form.values()]
    final = np.array(int_features)
    data_unseen = pd.DataFrame([final], columns = cols)
    prediction = predict_model(model, data=data_unseen, round = 0)
    prediction = int(prediction.Label[0])
    return render_template('home.html',pred='Expected Bill will be ${}'.format(prediction))

if __name__ == '__main__':
    app.run(debug=True)
