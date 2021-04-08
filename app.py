import numpy as np
from flask import Flask, render_template, request,jsonify
import pickle

app=Flask(_name_)
model=pickle.load(open('model.pkl','rb')) #loading pickle file in model variable

@app.route('/') #home route
def home():
    return render_template('input.html')
#predict route


@app.route('/predict', methods=['POST'])
def predict(): #for rendering ml model results on html gui

    #int_features=[request.form['experience'],request.form['test_score'],request.form['interview_score']]
    int_features=[int(x) for x in request.form.values()] #x is reading the 3 inputs from the form
    #all 3 values(features) are available in int_features

    final_features=[np.array(int_features)] #int_features converted into an array
    prediction=model.predict(final_features) #used the model from model.py file for predictions
    result=round(prediction[0],2) #rounds off a number to 2 decimal places
    return render_template('input.html',prediction_text='Employee s salary= ${}'.format(result))


@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if _name_ == "_main_":
    app.run(debug=True)
