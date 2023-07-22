import pickle

from django.shortcuts import render
import json
import numpy as np
from . import ppm

def get_started(request):
    return render(request, "index.html")

def predict(request):
    if request.method == 'POST':
        location_name = request.POST.get('location_name')
        square_feet = request.POST.get('squareFeet')
        bathroom = request.POST.get('bathroom')
        bhk = request.POST.get('bhk')

        # Convert square_feet, bathroom, and bhk to integers if they are valid
        try:
            square_feet = int(square_feet)
            bathroom = int(bathroom)
            bhk = int(bhk)
        except (ValueError, TypeError):
            square_feet = 0
            bathroom = 0
            bhk = 0

        # Call predict_price function to get the predicted price
        price = ppm.predict_price(location_name, square_feet, bathroom, bhk)

        # Round the price to 2 decimal places
        price = round(price, 2)

        # Pass user inputs and predicted price to the template
        return render(request, 'result.html', {
            'location': request.POST.get('location'),
            'squareFeet': square_feet,
            'bathroom': bathroom,
            'bhk': bhk,
            'price': price,
        })

    return render(request, 'result.html')