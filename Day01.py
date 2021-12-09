def countDepthIncreased(measurements):
    count = 0
    for i in range(1, len(measurements)):
        if measurements[i] > measurements[i-1]:
            count += 1
    return count

def countSlindingWindowDepthIncreased(measurements):
    prev_depth = 0
    count = -1
    for i in range(1, len(measurements) - 1):
        curr_depth = measurements[i - 1] + measurements[i] + measurements[i+1]
        if curr_depth > prev_depth:
            count +=1
        prev_depth = curr_depth
    return count


if __name__ == '__main__':
    with open('DataDay01.txt', 'r') as f:
        measurements =[int(entry )for entry in f.read().splitlines()]
        
    print(f'Depth increase count: {countDepthIncreased(measurements)}')
    print(f'Sliding Window depth increase count: {countSlindingWindowDepthIncreased(measurements)}')
    