from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_levels
from floodsystem.plot import polyfit
from floodsystem.stationdata import build_station_list, update_water_levels

# Test 2B


# Test 2E
def test_plot_water_levles(station, dates, levels):
    stations = build_station_list()
    update_water_levels(stations)
    for station in stations:
        if station.name == "Lecombe Basset":
            return "station has error"
            # As this station has an error

# Test 2F
def test_plot_water_levles(dates, levels, p):
    stations = build_station_list()
    update_water_levels(stations)
    for station in stations:
        assert polyfit == type(tuple) 
        # As the the funtion should return a tuple, asserting that it is a tuple 
