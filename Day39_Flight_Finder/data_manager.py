import requests
import os
from dotenv import load_dotenv

load_dotenv()

class DataManager:
    def __init__(self):
        self.sheety_endpoint = os.environ.get("SHEETY_ENDPOINT")
        self.sheety_headers = {
            "Authorization": f"Bearer {os.environ.get('SHEETY_API_KEY')}"
        }
        self.destination_data = {}

    def get_destination_data(self):
        """Fetch all destination data from Google Sheets"""
        response = requests.get(self.sheety_endpoint, headers=self.sheety_headers)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data["workouts"]  # Adjust sheet name
        return self.destination_data

    def update_destination_codes(self):
        """Update IATA codes in Google Sheets"""
        for city in self.destination_data:
            new_data = {
                "workout": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{self.sheety_endpoint}/{city['id']}",
                json=new_data,
                headers=self.sheety_headers
            )
            response.raise_for_status()
            print(f"✅ Updated {city['city']} with IATA code {city['iataCode']}")