from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
stations = build_station_list()
p = (52.2053, 0.1218)
print(stations_by_distance(stations, p)[:10])
print(stations_by_distance(stations, p)[-10:])