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

def parse_map(map_str:str) -> tuple[list, tuple, int]:
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


def vehicle_movement(map_str):
    def turn_right(v):
        """Turn the vehicle's direction 90 degrees to the right."""
        return (v[1], -v[0])

    obstacles, vehicle_position, map_size = parse_map(map_str)
    obstacles = set(obstacles)  # Convert to set for quick lookup
    visited_positions = set()  # Track unique positions visited

    current_position = vehicle_position
    direction = (0, 1)  # Initial direction: north (0,1)

    while True:
        visited_positions.add(current_position)

        next_position = (current_position[0] + direction[0], current_position[1] + direction[1])

        # Check bounds
        if (next_position[0] < 0 or next_position[1] < 0 or
                next_position[0] >= map_size or
                next_position[1] >= map_size):
            break

        if next_position in obstacles:
            direction = turn_right(direction)  # Turn right
        else:
            current_position = next_position  # Move to next position

    return len(visited_positions)


if __name__ == '__main__':
    with open('./data/data_06.txt') as f:
        data = f.read()

    print("Part 1:", vehicle_movement(data))