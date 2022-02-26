from .utils import sorted_by_key

#implement a function that returns a list of tuples, where each tuple holds
#(i) a station (object) at which the latest relative water level is over tol
#(ii) the relative water level at the station:
def stations_level_over_threshold(stations, tol):
  x=[]
  for station in stations:
    if station.relative_water_level() != None:
      if station.relative_water_level() > tol:
        s=(station.name, station.relative_water_level())
        x.append(s)
    x_sorted = sorted_by_key(x,1, reverse = True)
  return x_sorted
def stations_highest_rel_level(stations, N):
  #We want to return a list of N stations which have the highest water level relative to their typical range:
  high_level = stations_level_over_threshold( stations, 0)
  Highest = high_level[:N]
  return Highest
  
