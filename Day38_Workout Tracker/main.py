import requests
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Nutritionix API
NUTRITIONIX_APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
NUTRITIONIX_API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

# Sheety API
SHEETY_API_KEY = os.environ.get("SHEETY_API_KEY")
SHEETY_ENDPOINT = "https://api.sheety.co/your_username/your_project/your_sheet"

# Headers for Nutritionix
headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}

# User Input - What exercise did you do?
exercise_text = input("Tell me which exercise you did: ")

# Nutritionix API Request Parameters
parameters = {
    "query": exercise_text,
    "gender": "male",  # Change as per your gender
    "weight_kg": 70,   # Change to your weight
    "height_cm": 170,  # Change to your height
    "age": 25          # Change to your age
}

# Step 1: Get Exercise Data from Nutritionix
response = requests.post(NUTRITIONIX_ENDPOINT, json=parameters, headers=headers)
result = response.json()

# Extract exercise details
exercises = result.get("exercises", [])
if not exercises:
    print("❌ No exercises found. Please try again.")
    exit()

print(f"✅ Found {len(exercises)} exercise(s)!")

# Step 2: Prepare data for Google Sheets
today = datetime.now().strftime("%d/%m/%Y")
now = datetime.now().strftime("%H:%M:%S")

# Headers for Sheety
sheety_headers = {
    "Authorization": f"Bearer {SHEETY_API_KEY}"
}

# Step 3: Add each exercise to Google Sheets
for exercise in exercises:
    exercise_name = exercise["name"].title()
    duration = exercise["duration_min"]
    calories = exercise["nf_calories"]
    
    # Data format for Sheety
    sheet_data = {
        "workout": {
            "date": today,
            "time": now,
            "exercise": exercise_name,
            "duration": duration,
            "calories": calories
        }
    }
    
    # Step 4: Send data to Google Sheets via Sheety
    response = requests.post(SHEETY_ENDPOINT, json=sheet_data, headers=sheety_headers)
    
    if response.status_code == 200:
        print(f"✅ Added: {exercise_name} | {duration} min | {calories} calories")
    else:
        print(f"❌ Failed to add: {exercise_name}")
        print(f"Error: {response.text}")

print("\n🎉 All exercises added to your Google Sheet!")