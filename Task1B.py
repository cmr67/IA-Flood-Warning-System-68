from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

p = (52.2053, 0.1218)

def run():
    # Shell for 1B code to run
    # Builing the lists of stations and the distance of stations from the coordinate p
    stations = build_station_list()
    station_dist = stations_by_distance(stations, p)

    closest_ten = [] # Empty list for the 10 closest stations
    for station_d in station_dist [:10]:# Using the lowest 10 distances from p
        station, dist = station_d
        closest_ten.append((station.name, station.town, dist)) # Putting the station name, town and distance in to the list
    
    print("")
    print("The closest 10 stations are", closest_ten) # Printing the closest 10 stations
    print("")

    # Same explaination as closest 10, but now furthest 10
    furthest_ten = [] 
    for station_d in station_dist [-10:]:
        station, dist = station_d
        furthest_ten.append((station.name, station.town, dist))
    
    print("The furthest 10 stations are", furthest_ten)
    print("")

if __name__ == "__main__":
    print("")
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()