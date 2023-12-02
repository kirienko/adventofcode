def sum_of_possible_games(game_data):
    # Define the maximum number of cubes of each color
    max_cubes = {'red': 12, 'green': 13, 'blue': 14}

    possible_games_sum = 0

    # Process each game
    for game in game_data.split('\n'):
        if game.strip() == '':
            continue

        # Extract the game ID and the cube information
        game_id, cube_info = game.split(':')
        game_id = int(game_id.split(' ')[1])
        sets = cube_info.split(';')

        # Flag to check if the game is possible
        is_possible = True

        # Check each set of cubes revealed
        for set_ in sets:
            cubes = set_.split(',')
            for cube in cubes:
                parts = cube.strip().split(' ')
                if len(parts) < 2:  # Skip if no valid cube info
                    continue
                count, color = int(parts[0]), parts[1]
                # Check if the count exceeds the available cubes
                if count > max_cubes[color]:
                    is_possible = False
                    break
            if not is_possible:
                break

        # Add the game ID if the game is possible
        if is_possible:
            possible_games_sum += game_id

    return possible_games_sum


def sum_of_powers_of_minimum_sets(game_data):
    games_min_cubes = {}

    # Process each game
    for game in game_data.split('\n'):
        if game.strip() == '':
            continue

        # Extract the game ID and the cube information
        game_id, cube_info = game.split(':')
        game_id = int(game_id.split(' ')[1])
        sets = cube_info.split(';')

        min_cubes = {'red': 0, 'green': 0, 'blue': 0}

        # Check each set of cubes revealed
        for set_ in sets:
            cubes = set_.split(',')
            for cube in cubes:
                parts = cube.strip().split(' ')
                if len(parts) < 2:  # Skip if no valid cube info
                    continue
                count, color = int(parts[0]), parts[1]
                min_cubes[color] = max(min_cubes[color], count)

        # Calculate the power of the minimum set
        games_min_cubes[game_id] = min_cubes['red'] * min_cubes['green'] * min_cubes['blue']

    # Calculate and return the sum of the powers
    return sum(games_min_cubes.values())


with open('./data/data_02.txt') as fd:
    data = fd.read()

# Calculate and print the sum of the IDs of the possible games
print(sum_of_possible_games(data))
# Calculate and print the sum of the powers of the minimum sets
print(sum_of_powers_of_minimum_sets(data))
