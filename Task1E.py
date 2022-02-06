from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_stations_number
stations = build_station_list
n = 15
r = rivers_by_stations_number(stations, n)
print(r)
