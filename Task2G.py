from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level

def run():

    stations = build_station_list
    update_water_levels(stations)
    height=stations_highest_rel_level(stations)
    for station in stations:
        if height < (stations_highest_rel_level/2):
            print("Risk Level is Low")
        elif (stations_highest_rel_level/2) < height and height < (stations_highest_rel_level):
            print("Risk Level is Moderate")
        elif height > (stations_highest_rel_level) and height < (1.25*stations_highest_rel_level):
            print("Risk Level is High")
        elif height > (1.25*stations_highest_rel_level):
            print("Risk Level is evere")



if __name__ == "__main__":
    print("")
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()