

def parse_map(map_str:str) -> tuple[list, tuple, int]:
    """ Map coordinate system:
    [0,0] - bottom left
    x-axis increases to the right
    y-axis increases to the top
    """
    obstacles = []
    vehicle_position = None

    # Split the input string into lines and reverse to match the coordinate system
    lines = map_str.strip().split('\n')[::-1]

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == '#':
                obstacles.append((x, y))
            elif char == '^':
                vehicle_position = (x, y)

    return obstacles, vehicle_position, len(lines)


def vehicle_movement(obstacles, vehicle_position, map_size):
    def turn_right(v):
        """ Turn the vehicle's direction 90 degrees to the right """
        return v[1], -v[0]

    obstacles = set(obstacles)
    visited_positions = set()
    visited_states = set()

    current_position = vehicle_position
    direction = (0, 1)  # Initial direction is north (0,1)

    while True:
        visited_positions.add(current_position)
        visited_states.add((current_position, direction))

        next_position = (current_position[0] + direction[0], current_position[1] + direction[1])

        if (next_position[0] < 0 or next_position[1] < 0 or
                next_position[0] >= map_size or
                next_position[1] >= map_size):
            break       # Out of bounds
        elif (next_position, direction) in visited_states:
            return 0    # a loop was detected

        if next_position in obstacles:
            direction = turn_right(direction)
        else:
            current_position = next_position

    return len(visited_positions)


def all_obstacles(obstacles, vehicle_position, map_size):
    counter = 0
    for i in range(map_size):
        for j in range(map_size):
            if (i, j) not in obstacles + [vehicle_position]:
                if vehicle_movement(obstacles + [(i, j)], vehicle_position, map_size) == 0:
                    counter += 1

    return counter


if __name__ == '__main__':
    with open('./data/data_06.txt') as f:
        data = f.read()

    data = parse_map(data)
    print("Part 1:", vehicle_movement(*data))
    print("Part 2:", all_obstacles(*data))