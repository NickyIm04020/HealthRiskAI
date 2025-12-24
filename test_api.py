import requests
import json

# This script pretends to be a frontend app sending patient data
url = 'http://127.0.0.1:5000/predict'

# Fake patient data (20 features)
data = {
    "features": [65, 30.5, 8.2] + [0]*17  # Age 65, BMI 30.5, HbA1c 8.2, plus placeholders
}

try:
    response = requests.post(url, json=data)
    print("Status Code:", response.status_code)
    print("Response:", response.json())
except Exception as e:
    print("Error:", e)