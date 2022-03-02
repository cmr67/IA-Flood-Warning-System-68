from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_levels
from floodsystem.plot import polyfit
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold
from floodsystem.flood import stations_highest_rel_level

# Test 2B
def test_for_2B():
    s1 = MonitoringStation("test-s1-id", "test-m1-id", label= "station 1", coord = (-2.0, 4.0), trange= (0, 5), river= "River X", town= "My Town")
    s2 = MonitoringStation("test-s2-id", "test-m2-id", label = "station 2", coord = (-2.0, 4.0), trange= (0,5), river= "River Y", town= "My Town")
    s1.latest_level = 7
    s2.latest_level = 3
    stations_test=[s1,s2]
    tol = 1
    assert len(stations_level_over_threshold(stations_test, tol)) == 2
    assert stations_level_over_threshold(stations_test, tol)[0] == ('station 3', 1.0)
    assert stations_level_over_threshold(stations_test, tol)[1] == ('station 2', 0.6)
#Test 2C
def test_for_2C():
    s1 = MonitoringStation("test-s1-id", "test-m1-id", label= "station 1", coord = (-2.0, 4.0), trange= (0, 5), river= "River X", town= "My Town")
    s2 = MonitoringStation("test-s2-id", "test-m2-id", label = "station 2", coord = (-2.0, 4.0), trange= (0,5), river= "River Y", town= "My Town")
    s1.latest_level = 7
    s2.latest_level = 3
    stations_test=[s1,s2]
    assert len(stations_highest_rel_level(stations_test, length)) == 2
    assert stations_highest_rel_level(stations_test, length)[0] == ('station 3', 1.0)
    assert stations_highest_rel_level(stations_test, length)[1] == ('station 2', 0.6)

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
