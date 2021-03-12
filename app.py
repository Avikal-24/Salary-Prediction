import numpy as np
from flask import Flask , request , jsonify , render_template
import pickle

app= Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
# opening the pickle file in the read mode
# model is ready now in the variable 'model'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict' , methods=['POST'])
def predict():
    int_features= [int(x) for x in request.form.values()  ]
    final_features = [np.array(int_features)]
    predictions= model.predict(final_features)

    output= round(predictions[0],2)
    return render_template( 'index.html' , prediction_text= 'Employee salary should be $ {}'.format(output) )


if __name__=='__main__':
    app.run(debug=True)