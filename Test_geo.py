from haversine import haversine, Unit
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_stations_number
from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius

#test 1B
def test_stations_by_distance(stations, p):
  n=10
  for station in stations[-10:]:
    for i in range (n):
      assert stations_by_distance(stations, n)[i][1] < stations_by_distance(stations, n)[i-1][1]
    else:
      assert stations_by_distance(stations, n) == ('Boscadjack', 'Wendron', 440.00325604140033)

  for station in stations[10:]:
    for i in range (n):
      assert stations_by_distance(stations, n)[i][1] < stations_by_distance(stations, n)[i+1][1]
    else:
      assert stations_by_distance(stations, n) == ('Cambridge Jesus Lock', 'Cambridge', 0.840237595667494)

#test 1C
def test_stations_within_radius(stations, centre, r):
  stations = build_station_list()
  stations_in_radius = stations_within_radius(stations, (52.2053, 0.1218), 10)
  for station in stations_in_radius:
    assert haversine(station.coord, (52.2053, 0.1218)) <=10

#Test 1D
def test_rivers_with_station():
  stations=build_station_list()
  x= rivers_with_station(stations)
  assert len(x)==2165
  assert x[0]=='Addlestone Bourne'
  assert x[1]=='Adur'
def test_stations_by_river():
  stations = build_station_list()
  sbr_diction = stations_by_river(stations)
  assert type(sbr_diction) == type(dict())
  for key in sbr_diction.keys():
      for station in sbr_diction[key]:
          assert station.river == key
#task 1E           
def test_rivers_by_stations_number(stations, n):
  n=9
  for station in stations:
    for i in range(n):
      if i>0:
       assert rivers_by_stations_number(stations, n)[i][1] < rivers_by_stations_number(stations, n)[i-1][1]
      else:
        assert rivers_by_stations_number(stations, n)[i] == ('River Thames', 55)