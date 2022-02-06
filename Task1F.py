from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations


def run():
    # Shell for Task 1F
    # Building a list of stations where the station has inconststant typical range values 
    stations = build_station_list()
    inconsistent_range = inconsistent_typical_range_stations(stations)

    station_out_range = [] # Empty list
    for station in inconsistent_range: # Stations with inconsistant range 
        station_out_range.append(station.name) # Add the names of these stations to the list

    station_out_range.sort() # Sort the list in alphabetical order
    print(station_out_range) # Print the list
    print("")



if __name__ == "__main__":
    print("")
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    print("")
    run()