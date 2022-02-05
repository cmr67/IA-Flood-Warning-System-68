# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit

# Task 1B
def stations_by_distance(stations, p):
    listdistance = [] # Empty list
    for station in stations:
        dist = haversine(station.coord, p) # Distance between coordinates and the stations
        liststation=[station, dist]
        listdistance.append(liststation)
    return sorted_by_key(listdistance,1) # Sorting the distances in order

# Task 1C
def stations_within_radius(stations, centre, r):
    listradius = []
    for station in stations:
        distance_from_centre = haversine(station.coord, centre, unit=Unit.KILOMETERS) # Distance of the centre from the stations in km
        if distance_from_centre <= r: # If the distance is less than or equal to the specified radius, insclude it in the list
            listradius.append(station)
    return listradius
#Task 1D
def rivers_with_station(stations):
    river=[]
    for station in stations:
        if station.river in river:
            pass
        else:
            river.append(station.river)
    return sorted_by_key(river)
def stations_by_river(stations):
    station_riv = {}
    for station in stations:
        if station.river in station_riv.keys()
        station_riv[station.river].append(station.name)
    else:
        station_riv[station.river] = [station.name]
    
           
    
