from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import update_water_levels


def run():
    """Requirements for Task 2B"""

    # Build list of stations and set tolerance
    stations = build_station_list()
    tolerance=0.8
    
    #update
    update_water_levels(stations)
    
    # Print stations with ratio higher than tolerance
    print(stations_level_over_threshold(stations, tolerance))
    
if __name__ == "__main__":
    print("")
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    print("")
    run()
