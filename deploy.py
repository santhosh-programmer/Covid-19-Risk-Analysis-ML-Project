from flask import Flask,render_template,request
import numpy as np
import pickle

model=pickle.load(open('model_final.pkl','rb'))

app=Flask(__name__)

@app.route('/predict' , methods=["POST","GET"])
def predict():
    a=request.form.get('usmr')
    b=request.form.get('patient_type')
    c=request.form.get('pneumonia')
    d=request.form['age']
    e=request.form.get('diabetes')
    f=request.form.get('hypertension')
    g=request.form.get('renal_chronic')

    input=[a,b,c,d,e,f,g,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    h=request.form['medical_unit']
    input[5+int(h)]=1
    i=request.form['classification']
    input[17+ int(i)]=1

    input=np.array(input,dtype=int)

    print(input)
    input=input.reshape(1,25)
    prediction=model.predict(input)

    if(prediction[0]==2):
        ans="survive"
    else:
        ans=None
    
    return render_template('result1.html',answer=ans)

    


@app.route('/')
def main():
    return render_template('index.html')


app.run(debug=True)