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
        river.append(station.river)
        river.sort()
    return (river)
def stations_by_river(stations):
    station_riv = {}
    riv_w_station = rivers_with_station(stations)
    for river in riv_w_station:
        deez = []
        for station in stations:
            if station.river == river:
                deez.append(station.name)
        station_riv[river] = deez
    return station_riv   

#task 1E
def rivers_by_stations_number(stations, n):
    riv = stations_by_river(stations)
    riv_num = []
    for river in riv:        
        riv_num.append((river, len(riv[river])))
    riv_sorted = sorted_by_key(riv_num, 1, reverse=True)
    river_final = riv_sorted[:n]
    for river in riv_sorted:
        if river[1] == river_final[-1][1]:
            river_final.append(river)
        else:
            break
    return river_final