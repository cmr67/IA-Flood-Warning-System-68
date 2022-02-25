from .utils import sorted_by_key
from floodsystem.station import relative_water_level

#implement a function that returns a list of tuples, where each tuple holds
#(i) a station (object) at which the latest relative water level is over tol
#(ii) the relative water level at the station:
def stations_level_over_threshold(stations, tol):
  x=[]
  for station in stations:
    if station.relative_water_level() == None:
      if station.relative_water_level() > tol:
        x.append(station.name, station.relative_water_level())
   x_sorted = sorted_by_key(x,1, reverse = True)
   return x_sorted
def stations_highest_rel_level(stations, N):
  #We want to return a list of N stations which have the highest water level relative to their typical range:
  highest_N = stations_level_over_threshold( stations, 0)[N]
  return highest_N[:N]
  
