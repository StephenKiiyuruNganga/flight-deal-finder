import datetime as dt
from pprint import pprint
import requests


KIWI_BASE = "https://api.tequila.kiwi.com"
KIWI_API_KEY = "fvVtGvINbLoJPpsSOaQM4zf32lUZXV5Z"
LOCATIONS_API = "/locations/query"
SEARCH_API = "/v2/search"
KIWI_HEADERS = {
    "apikey": KIWI_API_KEY,
    "Content-Type": "application/json"
}

# --------- SEARCH CONSTANTS -----------
FLY_FROM = "NBO"  # Nairobi
CURRENCY = "KES"
FLIGHT_TYPE = "round"
NOW = dt.datetime.now()
DATE_FROM = (NOW + dt.timedelta(days=1)).strftime("%d/%m/%Y")
DATE_TO = (NOW + dt.timedelta(days=30*6)).strftime("%d/%m/%Y")
NIGHTS_FROM = 7
NIGHTS_TO = 28

# --------------------------------------


class FlightSearch:

    @staticmethod
    def getIATACode(city):
        query = {
            "term": city,
            "location_types": "city"
        }
        response = requests.get(
            url=KIWI_BASE+LOCATIONS_API, headers=KIWI_HEADERS, params=query)
        response.raise_for_status()
        code = response.json()["locations"][0]["code"]
        return code

    @staticmethod
    # def searchFlights(destination, lowest_price):
    def searchFlights(destination):
        query = {
            "fly_from": FLY_FROM,
            "fly_to": destination,
            "date_from ": DATE_FROM,
            "date_to": DATE_TO,
            "nights_in_dst_from": NIGHTS_FROM,
            "nights_in_dst_to": NIGHTS_TO,
            "one_for_city": 1,
            "max_stopovers": 0,
            "flight_type": FLIGHT_TYPE,
            "curr": CURRENCY,
            # "price_to": lowest_price,
        }
        response = requests.get(
            url=KIWI_BASE+SEARCH_API, headers=KIWI_HEADERS, params=query)
        response.raise_for_status()
        data = response.json()
        pprint(data)
