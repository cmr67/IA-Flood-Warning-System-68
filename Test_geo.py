from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
#Test 1D
def test_rivers_with_station():
  stations=build_by_station()
  x= rivers_with_station(stations)
  assert len(x)==843
  assert x[0]=='Addlestone Bourne'
  assert x[1]=='Adur'
def test_stations_by_river():
  stations = build_station_list()
    sbr_diction = stations_by_river(stations)
    assert type(sbr_diction) == type(dict())
    for key in sbr_diction.keys():
        for station in stations_by_river_dict[key]:
            assert station.river == key
def test_rivers_by_stations_number(stations, n):
  
