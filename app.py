# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 15:13:01 2019

@author: murat
"""

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle


#%%

app = Flask(__name__)
model = pickle.load(open("nb_model.pkl", "rb"))

#%%

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    if output == 0:
        return render_template('index.html', prediction_text = 'Üzgünüm! Kredi başvurunuz olumsuz sonuçlanmıştır.')
    else:
        return render_template('index.html', prediction_text = 'Harika! Kredi başvurunuz olumlu sonuçlanmıştır.')

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force = True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)

#%%



