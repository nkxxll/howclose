from .process_response import Coordinate


def test_haversine_distance():
    distance = 5585  # in km
    new_york = Coordinate(-74.00594, 40.71278)
    london = Coordinate(-0.12574, 51.50853)
    print(distance, round(new_york.haversine(london)))
    assert distance, round(new_york.haversine(london))
