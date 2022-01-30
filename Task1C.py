from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

centre = (52.2053, 0.1218)
r = 10

def run():
    #shell for 1C code
    stations = build_station_list
    stations_in_radius = stations_within_radius(stations, centre, r)

    station_list = []
    for station in stations_in_radius:
        station_list.append(station.name)

    print(sorted(stations_in_radius))

if __name__ == "__main__":
    print("")
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
