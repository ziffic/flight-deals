import requests
import connect

# This file will need to use the DataManager, FlightSearch, FlightData, NotificationManager
# classes to achieve the program requirements.

# TODO: 1. Use the Flight Search and Sheety API to populate your own copy of the Google Sheet with International Air
#           Transport Association (IATA) codes for each city. Most of the cities in the sheet include multiple
#           airports, you want the city code (not the airport code see at the link).

sheety_params = {
    "price": {
        "city": "Orange County",
        "iataCode": "",
        "lowestPrice": "500"
    }
}

sheety_response = requests.post(url=connect.SHEETY_ENDPOINT, json=sheety_params, headers=connect.sheety_headers)
# sheety_response = requests.get(url=connect.SHEETY_ENDPOINT, headers=connect.sheety_headers)
sheety_results = sheety_response.json()
print(sheety_results)
# TODO: 2. Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later for all the
#           cities in the Google Sheet.


# TODO: 3. If the price is lower than the lowest price listed in the Google Sheet then send an SMS to your own number
#           with the Twilio API.


# TODO: 4. The SMS should include the departure airport IATA code, destination airport IATA code, departure city,
#           destination city, flight price and flight dates. e.g.
