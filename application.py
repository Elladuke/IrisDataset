#!/usr/bin/env python
# coding: utf-8
import uvicorn
from Iris import Iris
from fastapi import FastAPI
import pickle

app = FastAPI()
import nest_asyncio
nest_asyncio.apply()
pickle_in = open('iris.pkl', "rb")
model = pickle.load(pickle_in)

@app.get('/')
def index():
    return{'message': "Flower prediction app"}

@app.get('/{name}')
def get_name(name: str):
    return{'Welcome to Ellas Flower prediction app': f'{name}'}

@app.post('/predict')
def predict_flower(data:Iris):
    data  = data.dict()
    print(data)
    print('Hello')
    petallength = data['petallength']
    sepallength =  data['sepallength']
    sepalwidth =  data['sepalwidth']
    petalwidth =  data['petalwidth']

   # print(model.predict([[petallength, sepallength, sepalwidth, petalwidth]]))
    print('Hello')
    prediction = model.predict([[petallength, sepallength, sepalwidth, petalwidth]])

    print("prediction value", prediction[0])
    if (prediction[0] == 0):
        prediction = 'This flower is iris-setosa'
    elif (prediction[0] == 1):
        prediction = 'This flower is iris versicolor'
    else:
        prediction = 'This flower is iris virginica'

    return {'prediction': prediction}

#run api with uvicorn
if __name__ == 'application':
    uvicorn.run(app, host = '127.0.0.1', port = 8000)
   # loop = asyncio.get_event_loop()
   # loop.run_until_complete(application())


