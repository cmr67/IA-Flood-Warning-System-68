from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

centre = (52.2053, 0.1218)
r = 10

def run():
    # Shell for 1C code
    # Builing the lists of stations and the stations within the radius r of the coordinates centre
    stations = build_station_list()
    stations_in_radius = stations_within_radius(stations, centre, r)

    station_list = [] # Empty list
    for station in stations_in_radius: # The stations within the radius
        station_list.append(station.name) # Append the stations name into the list
        
    station_list.sort # Sort the list

    for station in station_list:
        print(station) # Print the stations within the list
        print("")



if __name__ == "__main__":
    print("")
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    print("")
    run()