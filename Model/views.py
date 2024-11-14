from django.shortcuts import render
import joblib
import os
import pandas as pd

# Create your views here.
def home(request):
    if request.method == 'POST':
        bedrooms = request.POST['bedrooms']
        grade = request.POST['grade']
        basement = request.POST['basement']
        sqft_living = request.POST['sqft_living']
        renovated = request.POST['renovated']
        view = request.POST['view']
        conditions = request.POST['conditions']
        bathrooms = request.POST['bathrooms']
        lavatory = request.POST['lavatory']
        singleFloor = request.POST['singleFloor']
        month = request.POST['month']
        quartile = request.POST['quartile']
        
        price = pricePrediction(request, bedrooms, grade, basement, sqft_living, renovated, view, conditions, bathrooms, lavatory, singleFloor, month, quartile)
        price = "{:,}".format(price)
        
        return render(request , 'home.html' , {'price':price})
    
    return render(request , 'home.html')

def pricePrediction(request, bedrooms, grade, basement, sqft_living, renovated, view, conditions, bathrooms, lavatory, singleFloor, month, quartile):
    
    predictedPrice = 0
    
    #df = pd.DataFrame({bedrooms, grade, basement, sqft_living, renovated, view, conditions, bathrooms, lavatory, singleFloor, month, quartile})
    
    model = joblib.load(os.path.join(os.path.dirname(__file__) , 'random_forest_model.pkl'))
    
    predictedPrice = int(model.predict([[bedrooms, grade, basement, sqft_living, renovated, view, conditions, bathrooms, lavatory, singleFloor, month, quartile]]))
    
    return predictedPrice