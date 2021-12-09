import pandas as pd


def parse_input(filename):
    with open(filename, 'r') as f:
        df = pd.DataFrame([entry.split(' ') for entry in f.read().splitlines()], columns=['Direction', 'Steps']).astype({'Direction': str, 'Steps': int})
        
    return df


def calculate_final_position(directions):
    steps = df.groupby('Direction').sum().to_dict()['Steps']
    depth = aim = steps['down'] - steps['up']
    return depth, steps['forward']


def calculate_final_position_aim(directions):
    directions = directions.to_dict('records')
    aim = 0
    horizontal = 0
    depth = 0
    for entry in directions:
        step_size = entry['Steps']
        direction = entry['Direction']
        if direction  == 'up':
            aim -= step_size
        elif direction == 'down':
            aim += step_size
        else:
            horizontal += step_size
            depth += aim * step_size
            
    return horizontal, depth


if __name__ == '__main__':
    df = parse_input('DataDay02.txt')
    depth, horizontal = calculate_final_position(df)
    depth_2, horizontal_2 = calculate_final_position_aim(df)
    print(f'Multiplied final position: {depth * horizontal}')
    print(f'Final positionusing aim: {depth_2 * horizontal_2}')