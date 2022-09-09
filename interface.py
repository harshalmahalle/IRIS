from flask import Flask,render_template,jsonify,request
from project_iris.utiles import iries_flower
import config

app=Flask(__name__)

@app.route('/home')
def home():
    return 'omm'

@app.route('/mira')
def flowers():
    SepalLengthCm=4.5
    SepalWidthCm=2.0
    PetalLengthCm=5.3
    PetalWidthCm=2.5 
    p=iries_flower(SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm)  
    charges=p.get_spacies()
    return jsonify({"Result": f"Predicted isS : {charges}"})

    # med_ins = MedicalInsurence(age, sex, bmi,children,smoker, region)
    #     charges = med_ins.get_predicted_charges()

app.run()
