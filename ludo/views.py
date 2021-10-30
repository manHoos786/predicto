from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
import joblib



# Create your views here.

def home(request):
    return render(request,'home.html')


def result(request):
    if request.method == 'POST':
        
        km = int(request.POST['kms'])
        fuel = int(request.POST['fuel_type'])
        trans = int(request.POST['trans'])
        deal = int(request.POST['dealer'])
        mile = float(request.POST['mileage'])
        engine = int(request.POST['engine'])
        price = int(request.POST['price'])
        power = float(request.POST['max'])
        seat = int(request.POST['seat'])
        comp = int(request.POST['company'])
        age = int(request.POST['age'])
    
        model = joblib.load('Final_effort.pkl')
        prediction=model.predict([[comp,age,km,deal,fuel,trans,mile,engine,power,seat,price]])
        output=round(prediction[0],2)

        context = {
    
            'km':km,
            'fuel':fuel,
            'deal':deal,
            'trans':trans,
            'mile':mile,
            'engine':engine,
            'power':power,
            'seat':seat,
            'comp':comp,
            'age':age,
            'aaaanshi':output
            
        }
        print(output)

       
        return render(request,'result.html',context)
    

