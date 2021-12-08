import time


def main():
    input = standard_func.get_input_as_str('input.txt')[0]
    # input = standard_func.get_input_as_str('test.txt')[0]
    s = input
    iterations = 40

    for _ in range(iterations):
        # print('iteration', _)
        # print('s', s)
        char_repetition_count = 0
        next_s = ''
        curr_char = s[0]

        for c in s:
            if c == curr_char:
                char_repetition_count += 1
            else:
                next_s += str(char_repetition_count) + curr_char
                curr_char = c
                char_repetition_count = 1

        next_s += str(char_repetition_count) + curr_char
        s = next_s

    print(len(s))


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
