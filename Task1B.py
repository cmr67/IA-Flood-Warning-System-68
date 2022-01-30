from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

p = (52.2053, 0.1218)

def run():
    # shell for 1B code to run
    stations = build_station_list()
    station_dist = stations_by_distance(stations, p)

    closest_ten = []
    for station_d in station_dist [:10]:
        station, dist = station_d
        closest_ten.append((station.name, station.town, dist))
    
    print("")
    print("The closest 10 stations are", closest_ten)
    print("")

    furthest_ten = []
    for station_d in station_dist [-10:]:
        station, dist = station_d
        furthest_ten.append((station.name, station.town, dist))
    
    print("The furthest 10 stations are", furthest_ten)
    print("")

if __name__ == "__main__":
    print("")
    print("Task 1B")
    run()