# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""


#from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit

def stations_by_distance(stations, p):
    for station in stations:
        list_stations=[station.name, haversine(station.coordinates, p)]
    return list_stations
print(stations_by_distance(station.coordinates(23,12), p(12,23)))        
