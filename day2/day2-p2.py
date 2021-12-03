import time

def get_lwh(input):
    return sorted(list(map(lambda a : int(a), input.split('x'))))

def main():
    dims = get_input_as_str('input.txt')
    # dims = get_input_as_str('test.txt')
    total_ribbon = 0

    for dim in dims:
        l, w, h = get_lwh(dim)
        total_ribbon += 2*l + 2*w + l*w*h  # l and w are smallest dimensions because input row in sorted

    print(total_ribbon)

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
