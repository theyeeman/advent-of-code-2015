import time


def calc_encoded_length(s):
    added_len = 0

    for char in s:
        if char == '\\' or char == '"':
            added_len += 1

    return len(s) + added_len + 2  # +2 is for the front and end quotation marks


def main():
    inputs = standard_func.get_input_as_str('input.txt')
    # inputs = standard_func.get_input_as_str('test.txt')
    
    raw_length = 0
    encoded_length = 0

    for input in inputs:
        raw_length += len(input)
        encoded_length += calc_encoded_length(input)

    print(encoded_length - raw_length)


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
