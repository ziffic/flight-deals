import requests
import connect

# Populate the Google Sheet with IATA codes
# sheety_response = requests.get(url=connect.SHEETY_ENDPOINT)
# sheety_results = sheety_response.json()

# for record in sheety_results["prices"]:
#     kiwi_params = {
#         "term": record["city"]
#     }
#
#     kiwi_response = requests.get(url=connect.KIWI_ENDPOINT, params=kiwi_params, headers=connect.KIWI_HEADERS)
#     kiwi_data = kiwi_response.json()
#
#     sheety_params = {
#         "price": {
#             "iataCode": kiwi_data["locations"][0]["code"]
#         }
#     }
#     sheety_response = requests.put(url=f"{connect.SHEETY_ENDPOINT}/{record['id']}", json=sheety_params)


sheety_response = requests.get(url=connect.SHEETY_ENDPOINT)
sheety_results = sheety_response.json()

ENDPOINT = "https://api.tequila.kiwi.com/v2/search?"

for record in sheety_results["prices"]:
    kiwi_params = {
        "fly_from": "LON",
        "fly_to": record["iataCode"],
        "dateFrom": "04/06/2023",
        "dateTo": "10/06/2023",
        "max_stopovers": 0,
        "curr": "GBP",
    }

    kiwi_response = requests.get(url=ENDPOINT, params=kiwi_params, headers=connect.KIWI_HEADERS)
    kiwi_data = kiwi_response.json()
    print(f"{record['city']} {kiwi_data['data'][0]['price']}")
