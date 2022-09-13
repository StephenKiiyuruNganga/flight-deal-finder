# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from pprintpp import pprint


dataManager = DataManager()
dataManager.getFlightData()

# pprint(dataManager.flight_data)

sheet_data = dataManager.data

# for row in sheet_data:
#     code = FlightSearch.getIATACode(row["city"])
#     if not row["iataCode"]:
#         dataManager.updateRow(row["id"], "iataCode", code)

FlightSearch.searchFlights("PAR")
