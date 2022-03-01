from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels
import datetime
import matplotlib as plt
from floodsystem.utils import sorted_by_key

def run():
    #Shell for Task 2E
    stations = build_station_list() 
    update_water_levels(stations) #Updating the water levels
    High_Water = [] # Empty list
    for station in stations:
        if station.latest_level != None: # If the lastest water levels are not = to none 
            #amend the station name and the water level into the list, else pass it
            High_Water.append((station.name, station.latest_level))
        else:
            pass
    sorted_list = sorted_by_key(High_Water, 1, True)[:5] # Sort the list for the 5 highest relative water levels
    name_list = [] # Empty list
    for i in range(5): # range for the 5 water stations that are the highest
        name_list.append(sorted_list[i][0]) # append the sorted statioons into the list
    print(sorted_list) # print the list
    dt=10 # past 10 days
    for station in stations:
        for i in range(5):
            if station.name == name_list[i]: # if the name of the station is in the station list
                print(station.name) # print the station name
                dates, levels = fetch_measure_levels(station.measure_id,dt = datetime.timedelta(dt))
                plot_water_levels(station, dates, levels) # plot the station in that list for the past 10 days
                # with the dates at the water levels for that station  

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()