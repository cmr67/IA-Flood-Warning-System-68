from floodsystem.plot import plot_water_levels
from datetime import datetime, timedelta
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
import matplotlib
import matplotlib.pyplot as plt

def run():
    # Shell for 2E
    # Updating all of the water levels for the stations
    station = build_station_list
    update_water_levels(station)
    highest_relative_levels = stations_highest_rel_level(station, 5) # 5 stations with highest relative water levels
    dt = 10 # Past 10 days

    for station in highest_relative_levels:
        dates, levels = fetch_measure_levels(station.measure_id, dt)
        plot_water_levels(station, dates, levels)

        plt.show()

if __name__ == "__main__":
    print("")
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()