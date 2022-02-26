from floodsystem.plot import plot_water_level_with_fit
import matplotlib
import matplotlib.pyplot as plt
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():
    # Shell for Task 2F
    # Updating all of the water levels for the stations
    stations = build_station_list()
    update_water_levels(stations)
    highest_relative_levels = stations_highest_rel_level(stations, 5) # 5 stations with highest relative water levels
    
    dt = 2 # Past 2 days
    p = 4 # Polynomial with a degree of 4
    
    for station in highest_relative_levels:
        dates, levels = fetch_measure_levels(station.measure_id, dt) # Fetching the updated water levels for the past 10 days
        plot_water_level_with_fit(dates, levels, p)

if __name__ == "__main__":
    print("")
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()