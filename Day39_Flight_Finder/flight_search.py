import requests
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

class FlightSearch:
    def __init__(self):
        self.tequila_endpoint = "https://tequila-api.kiwi.com/v2/search"
        self.tequila_headers = {
            "apikey": os.environ.get("TEQUILA_API_KEY")
        }

    def get_iata_code(self, city_name):
        """Get IATA code from city name"""
        location_endpoint = "https://tequila-api.kiwi.com/locations/query"
        params = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(
            location_endpoint,
            headers=self.tequila_headers,
            params=params
        )
        response.raise_for_status()
        data = response.json()
        
        if data["locations"]:
            return data["locations"][0]["code"]
        return None

    def search_flights(self, origin_city_code, destination_city_code, 
                       from_time, to_time, price_limit, currency="INR"):
        """Search for flights between cities"""
        tomorrow = datetime.now() + timedelta(days=1)
        six_months = datetime.now() + timedelta(days=180)
        
        params = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": tomorrow.strftime("%d/%m/%Y"),
            "date_to": six_months.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "INR"
        }
        
        response = requests.get(
            self.tequila_endpoint,
            headers=self.tequila_headers,
            params=params
        )
        response.raise_for_status()
        
        try:
            data = response.json()
            flights = data.get("data", [])
            
            if not flights:
                print(f"❌ No direct flights found for {destination_city_code}")
                return None
            
            # Return first flight (cheapest)
            return self._parse_flight_data(flights[0])
        except Exception as e:
            print(f"Error searching flights: {e}")
            return None

    def _parse_flight_data(self, flight):
        """Parse flight data into FlightData object"""
        from datetime import datetime as dt
        
        return FlightData(
            price=flight["price"],
            origin_city=flight["cityFrom"],
            origin_airport=flight["flyFrom"],
            destination_city=flight["cityTo"],
            destination_airport=flight["flyTo"],
            out_date=dt.fromtimestamp(flight["dTime"]).strftime("%d/%m/%Y"),
            return_date=dt.fromtimestamp(flight["aTime"]).strftime("%d/%m/%Y")
        )