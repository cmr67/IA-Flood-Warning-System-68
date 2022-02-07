from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_stations_number

def run ():
    stations = build_station_list() 
    n = 9
    print(rivers_by_stations_number(stations, n))
if __name__ == "__main__":
    print("")
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    print("")
    run()