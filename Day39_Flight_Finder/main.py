from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager # type: ignore
import os
from dotenv import load_dotenv

load_dotenv()

def main():
    # Initialize classes
    data_manager = DataManager()
    flight_search = FlightSearch()
    notification_manager = NotificationManager()
    
    # Step 1: Get destination data from Google Sheets
    print("📊 Fetching destinations from Google Sheets...")
    destinations = data_manager.get_destination_data()
    
    # Step 2: Update IATA codes if missing
    for destination in destinations:
        if not destination.get("iataCode"):
            print(f"🔍 Getting IATA code for {destination['city']}")
            iata_code = flight_search.get_iata_code(destination["city"])
            if iata_code:
                destination["iataCode"] = iata_code
                data_manager.update_destination_codes()
            else:
                print(f"❌ Could not find IATA code for {destination['city']}")
    
    # Step 3: Search for flight deals
    ORIGIN_CITY = "DEL"  # Change to your nearest airport
    price_limit = 10000  # Maximum price in INR
    
    for destination in destinations:
        if not destination.get("iataCode"):
            continue
            
        print(f"\n✈️ Searching flights to {destination['city']} ({destination['iataCode']})...")
        
        flight = flight_search.search_flights(
            origin_city_code=ORIGIN_CITY,
            destination_city_code=destination["iataCode"],
            from_time=1,
            to_time=180,
            price_limit=price_limit
        )
        
        if flight and flight.price < destination.get("lowestPrice", 10000):
            # If flight is cheaper than stored price, send notification
            message = f"""
🔊 FLIGHT DEAL ALERT! 🔊

✈️ From: {flight.origin_city} ({flight.origin_airport})
✈️ To: {flight.destination_city} ({flight.destination_airport})
💰 Price: ₹{flight.price}
📅 Out Date: {flight.out_date}
📅 Return Date: {flight.return_date}
            """
            print(message)
            notification_manager.send_sms(message)
            notification_manager.send_email("Flight Deal Alert!", message)
        elif flight:
            print(f"📊 Price to {destination['city']}: ₹{flight.price}")
        else:
            print(f"❌ No flights found to {destination['city']}")

if __name__ == "__main__":
    main()