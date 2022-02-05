from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
stations = build_stations_list()
x=sorted(rivers_with_station(stations))
x_first10=x[:10]
print("the rivers thathave monitoring stations are:", x_first10)
print("the number of stations are:", len(x)) 
y= stations_by_river(stations)
river_aire = y["River Aire"]
sorted_ra = sorted(river_aire)
river_cam = y["River Cam"]
sorted_rc = sorted(river_cam)
river_thames=y["River Thames"]
sorted_rt = sorted(river_thames)
print("River Aire", sorted_ra)
print("River Cam", sorted_rc)
print("River Thames", sorted_rt)
