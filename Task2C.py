from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():
    """Requirements for Task 2C"""

    # Build list of stations
    stations = build_station_list()
    # we want to print the first 10 when N = 10:
    # before let's update the data:
    update_water_levels(stations)
    # now we print:
    print(stations_highest_rel_level(stations, 10)) 

if __name__ == "__main__":
    print("")
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    print("")
    run()
