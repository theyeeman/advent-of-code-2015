import time


def grid_action(grid, command, x1, y1, x2, y2):
    if command == 'on':
        turn_on(grid, x1, y1, x2, y2)
    elif command == 'off':
        turn_off(grid, x1, y1, x2, y2)
    else:
        toggle(grid, x1, y1, x2, y2)


def turn_on(grid, x1, y1, x2, y2):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            grid[i][j] = 1


def turn_off(grid, x1, y1, x2, y2):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            grid[i][j] = 0


def toggle(grid, x1, y1, x2, y2):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            grid[i][j] = 1 if grid[i][j] == 0 else 0


def parse_input_row(input):
    s = input.split(' ')
    if len(s) == 4:  # Toggle
        x1, y1 = s[1].split(',')
        x2, y2 = s[3].split(',')
        return ('toggle', int(x1), int(y1), int(x2), int(y2))

    if s[1] == 'on':
        x1, y1 = s[2].split(',')
        x2, y2 = s[4].split(',')
        return ('on', int(x1), int(y1), int(x2), int(y2))
    else:
        x1, y1 = s[2].split(',')
        x2, y2 = s[4].split(',')
        return ('off', int(x1), int(y1), int(x2), int(y2))


def count_lights_on(grid):
    count = 0

    for row in grid:
        for col in row:
            if col == 1:
                count += 1

    return count


def main():
    inputs = standard_func.get_input_as_str('input.txt')
    # inputs = standard_func.get_input_as_str('test.txt')
    grid_row = [0] * 1000
    grid = []

    for _ in range(1000):
        grid.append(grid_row.copy())
    
    for input in inputs:
        command, x1, y1, x2, y2 = parse_input_row(input)
        grid_action(grid, command, x1, y1, x2, y2)

    print(count_lights_on(grid))


# Boilerplate code below
class standard_func:
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
    standard_func.print_performance(perf_counter_start, perf_counter_end)
