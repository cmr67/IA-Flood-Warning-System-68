from floodsystem.plot import plot_water_levels
from datetime import datetime, timedelta
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
import matplotlib.pyplot as plt

def run():
    # Shell for 2E
    # Updating all of the water levels for the stations
    stations = build_station_list()
    update_water_levels(stations)
    highest_relative_levels = stations_highest_rel_level(stations, 5) # 5 stations with highest relative water levels
    stations_plot = []
    i = 0

    dt = 10 # Past 10 days
    for station in highest_relative_levels:
        for i in stations:
            if station[0] == [i]:
                stations_plot.append[i]

    for i in stations_plot:
        dates, levels = fetch_measure_levels(i.measure_id, 
                                dt=datetime.timedelta(days=dt)) # Fetching the updated water levels for the past 10 days
                
        plot_water_levels(i, dates, levels)# Shows the plot/results

    

if __name__ == "__main__":
    print("")
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
