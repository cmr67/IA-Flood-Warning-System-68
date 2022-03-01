from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit
import datetime
from floodsystem.utils import sorted_by_key
 



def run():
    # Shell for Task 2F
    # Updating all of the water levels for the stations
    stations = build_station_list() 
    update_water_levels(stations)
    highest_relative_levels = [] # Empty list
    for station in stations: 
        if station.latest_level == None: # Make sure that excluding the station with none from system
            pass
        elif station.latest_level >= 90: # if more than 90 exclude from system as exceed limit
            pass
        else:
            highest_relative_levels.append((station.name, station.latest_level)) 
            # append the name and level into list if not already removed
    sorted = sorted_by_key(highest_relative_levels, 1, True)[:5]
    names = [] # Empty List
    for i in range(5): # range of 5
        names.append(sorted[i][0]) # Append the sorted relative water levels into the list
    print(sorted) # print the list

    dt = 2 # Past 2 days
    p = 4 # Polynomial with a degree of 4

    for station in stations:
        for i in range (5): # Range of 5
            if station.name == names[i]: # if names of station in in the list of the range
                print(station.name)  # print these names
                dates, levels = fetch_measure_levels(station.measure_id, dt = datetime.timedelta(days = dt))
                # Fetching the updated water levels for the past 2 days
                plot_water_level_with_fit(station, dates, levels, p) # Plot it


if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()