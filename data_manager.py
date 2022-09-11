import requests

SHEETY_API = "https://api.sheety.co/8e7a7dc2a8849028d5c9c103dd334896/flightDeals/prices"
SHEETY_API_KEY = "St3vAn0v1c"
SHEETY_HEADERS = {
    "Authorization": f"Bearer {SHEETY_API_KEY}"
}


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.data = None

    def getFlightData(self):
        response = requests.get(url=SHEETY_API, headers=SHEETY_HEADERS)
        response.raise_for_status()
        data = response.json()
        self.data = data["prices"]

    def updateRow(self, id, column_name, value):
        body = {
            "price": {
                column_name: value
            }
        }
        response = requests.put(
            url=f"{SHEETY_API}/{id}", json=body, headers=SHEETY_HEADERS)
        response.raise_for_status()
        data = response.json()
        print(data)
