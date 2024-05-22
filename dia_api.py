from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

app = FastAPI()

class model_input(BaseModel):
    pregnancies : int
    Glucose : int
    BloodPressure : int
    SkinThickness : int
    Insulin : float
    BMI : float
    DiabetesPedigreeeFunction: float
    Age : int

# Loading the saved model
diabetes_model = pickle.load(open('trained_model.sav','rb'))

@app.post('/diabetes_pred')

def daibetes_pred(input_param: model_input):
    input_data = input_param.json()
    input_dic = json.loads(input_data)
    
    # Convert the dictionary ti tuple
    preg = input_dic['pregnancies']
    glu = input_dic['Glucose']
    bp = input_dic['BloodPressure']
    skin = input_dic[' SkinThickness']
    insulin = input_dic['Insulin']
    bmi = input_dic['BMI']
    dpf = input_dic['DiabetesPedigreeeFunction']
    age = input_dic['Age']

    input_list = [preg, glu, bp, skin, insulin, bmi, dpf, age]

    prediction = diabetes_model.predict([input_list])

    if prediction[0] == 0:
        return " The person is not Diabetic"
    else:
        return " The preson is Diabetic"