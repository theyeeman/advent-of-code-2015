import time

def main():
    directions = get_input_as_str('input.txt')[0]
    # directions = get_input_as_str('test.txt')[0]
    x = 0
    y = 0
    visited = set()
    visited.add((x, y))
    
    for direction in directions:
        match direction:
            case '<':
                x += 1
            case '>':
                x -= 1
            case '^':
                y += 1
            case 'v':
                y -= 1
            case _:
                print("invalid direction")
        
        visited.add((x, y))

    print(len(visited))

# Boilerplate code below

def get_input_as_int(filename):
    with open(filename) as f:
        return list(map(lambda a : int(a), list((f.read()).split("\n"))))

def get_input_as_str(filename):
    with open(filename) as f:
        return list((f.read()).split("\n"))

def print_performance(start, end):
    print('Execution time (s):', round((end - start), 3))

if __name__ == "__main__":
    perf_counter_start = time.perf_counter()
    main()
    perf_counter_end = time.perf_counter()
    print_performance(perf_counter_start, perf_counter_end)
