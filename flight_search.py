from pprint import pprint
import requests


KIWI_BASE = "https://api.tequila.kiwi.com"
KIWI_API_KEY = "fvVtGvINbLoJPpsSOaQM4zf32lUZXV5Z"
LOCATIONS_API = "/locations/query"

KIWI_HEADERS = {
    "apikey": KIWI_API_KEY,
    "accept": "application/json"
}


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
