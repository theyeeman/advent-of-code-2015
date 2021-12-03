import time

def main():
    directions = get_input_as_str('input.txt')[0]
    # directions = get_input_as_str('test.txt')[0]
    x_s = 0  # Santa
    y_s = 0
    x_r = 0  # Robo
    y_r = 0
    visited = set()
    visited.add((0, 0))
    flipflop = True
    
    for direction in directions:
        if flipflop:  # Santa moves
            flipflop = False

            match direction:
                case '<':
                    x_s += 1
                case '>':
                    x_s -= 1
                case '^':
                    y_s += 1
                case 'v':
                    y_s -= 1
                case _:
                    print("invalid direction")
            
            visited.add((x_s, y_s))
        
        else:  # Robo moves
            flipflop = True

            match direction:
                case '<':
                    x_r += 1
                case '>':
                    x_r -= 1
                case '^':
                    y_r += 1
                case 'v':
                    y_r -= 1
                case _:
                    print("invalid direction")
            
            visited.add((x_r, y_r))

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
