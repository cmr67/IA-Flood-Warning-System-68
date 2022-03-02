from distutils.command.build import build
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import *
from floodsystem.analysis import flood_warning
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
import datetime

def run():

    stations = build_station_list()
    update_water_levels(stations)
    low,moderate,high,severe = sorted(flood_warning(stations))
    list_low =[]
    list_moderate=[]
    list_high=[]
    list_severe=[]
    for i in range(len(low)):
        list_low.append(low[i][0])
    for i in range(len(moderate)):
        list_moderate.append(moderate[i][0])
    for i in range(len(high)):
        list_high.append(high[i][0])
    for i in range(len(severe)):
        list_severe.append(severe[i][0])

    print("low", list_low)
    print("")
    print("moderate", list_moderate)
    print("")
    print("high", list_high)
    print("")
    print("severe", list_severe)

if __name__ == "__main__":
    print("")
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()