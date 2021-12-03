import time

def get_lwh(input):
    return sorted(list(map(lambda a : int(a), input.split('x'))))

def main():
    dims = get_input_as_str('input.txt')
    # dims = get_input_as_str('test.txt')
    total_area = 0

    for dim in dims:
        l, w, h = get_lwh(dim)
        total_area += 2*l*w + 2*w*h + 2*h*l + l*w  # l and w are smallest dimensions because input row in sorted

    print(total_area)

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
