import requests
import os
from twilio.rest import Client

# API Keys from environment variables
API_KEY = os.environ.get("OWM_API_KEY")
TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_AUTH = os.environ.get("TWILIO_AUTH")

# Weather API parameters
parameters = {
    "lat": YOUR_LAT,
    "lon": YOUR_LON,
    "appid": API_KEY,
    "exclude": "current,minutely,daily",
    "cnt": 4
}

# Fetch weather data
response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()

# Check if it will rain in next 12 hours
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

# Send SMS alert if it will rain
if will_rain:
    client = Client(TWILIO_SID, TWILIO_AUTH)
    message = client.messages.create(
        body="🌧️ It's going to rain today! Bring an umbrella ☂️",
        from_=TWILIO_PHONE,
        to=YOUR_PHONE
    )
    print("✅ Alert sent!")
else:
    print("☀️ No rain expected today!")