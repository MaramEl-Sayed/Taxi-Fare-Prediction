from django.shortcuts import render
from tensorflow.keras.models import load_model
import numpy as np
import os
from django.conf import settings

# Load the model once when the module is loaded
model_path = os.path.join(settings.BASE_DIR, 'myAPP', 'Models', 'model.h5')
model = load_model(model_path)

# Define the mappings for categorical features
car_condition_mapping = {
    'Bad': 0,
    'Good': 1,
    'Very Good': 2,
    'Excellent': 3
}

weather_condition_mapping = {
    'Sunny': 0,
    'Cloudy': 1,
    'Rainy': 2,
    'Stormy': 3,
    'Windy': 4
}

traffic_condition_mapping = {
    'Congested Traffic': 0,
    'Dense Traffic': 1,
    'Flow Traffic': 2
}
def predict(request):
    return render(request, 'index.html')

def formInfo(request):
    # Get input values from request
    car_condition = car_condition_mapping[request.GET['car_condition']]
    traffic_condition = traffic_condition_mapping[request.GET['traffic_condition']]
    weather_condition = weather_condition_mapping[request.GET['weather_condition']]
    passenger_count = int(request.GET['passenger_count'])
    hour = int(request.GET['hour'])   
    month = int(request.GET['month'])
    week_day = int(request.GET['week_day'])
    day = int(request.GET['day'])   
    pickup_longitude = float(request.GET['pickup_longitude'])
    pickup_latitude = float(request.GET['pickup_latitude'])
    dropoff_longitude = float(request.GET['dropoff_longitude'])
    dropoff_latitude = float(request.GET['dropoff_latitude'])
    jfk_dist = float(request.GET['jfk_dist'])
    sol_dist = float(request.GET['sol_dist'])
    lga_dist = float(request.GET['lga_dist'])
    ewr_dist = float(request.GET['ewr_dist'])
    nyc_dist = float(request.GET['nyc_dist'])
    distance = float(request.GET['distance'])
    bearing = float(request.GET['bearing'])

    # Prepare the input for the model
    input_data = np.array([[car_condition, traffic_condition, weather_condition, pickup_longitude, 
                            pickup_latitude, dropoff_longitude, dropoff_latitude, passenger_count, 
                            hour, day, month, week_day, jfk_dist, ewr_dist,lga_dist, sol_dist, 
                            nyc_dist,distance, bearing]])

    # Make prediction
    y_pred = model.predict(input_data)
    
    # Assuming the model's output is a single value, you might want to format it
    prediction_result = y_pred[0][0]  # Adjust indexing based on your model's output shape

    # Pass the prediction result to the result template
    return render(request, 'result.html', {'prediction': prediction_result})