from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import town
stations = build_station_list()
townlocation = town
p = (52.2053, 0.1218)
print(stations_by_distance(stations, townlocation, p)[:10])
print(stations_by_distance(stations, townlocation, p)[-10:])