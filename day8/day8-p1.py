import time


def create_py_file(inputs):
    f = open('day8-generated-p1.py', 'a')
    f.write("rep_length = 0\n")

    for input in inputs:
        f.write(f"rep_length += len({input})\n")

    f.write("print(f'rep_length: {rep_length}')\n")

    f.close()


def main():
    inputs = standard_func.get_input_as_str('input.txt')
    # inputs = standard_func.get_input_as_str('test.txt')
    
    raw_length = 0

    for input in inputs:
        raw_length += len(input)

    print(f'raw_length: {raw_length}')
    create_py_file(inputs)
    # Run the generated file "day8-generated-p1.py" to get representational length


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
