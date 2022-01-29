# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit

def stations_by_distance(stations, p):
    listdistance=[]
    for station in stations:
        liststation=[station.name, haversine(station.coord, p)]
        listdistance.append(liststation)
    return sorted_by_key(listdistance,1)     
