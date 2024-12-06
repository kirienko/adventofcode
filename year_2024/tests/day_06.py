from year_2024.day_06 import all_obstacles, parse_map, vehicle_movement

map_str = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""
obstacles, vehicle_position, map_size = parse_map(map_str)


def test_parse_map():
    obstacles, vehicle_position, map_size = parse_map(map_str)
    assert obstacles == [(6, 0), (0,1),(8, 2), (1, 3), (7, 5), (2, 6), (9, 8), (4, 9)]
    assert vehicle_position == (4, 3)
    assert map_size == 10

def test_vehicle_movement():
    """ Check Part 1 example solution """
    assert vehicle_movement(obstacles, vehicle_position, map_size) == 41

def test_loop():
    """ Check that the loop is detected """
    new_obstruction = (7, 0)
    assert vehicle_movement(obstacles + [new_obstruction], vehicle_position, map_size) == 0

def test_all_obstacles():
    """ Check Part 1 example solution """
    assert all_obstacles(obstacles, vehicle_position, map_size) == 6
