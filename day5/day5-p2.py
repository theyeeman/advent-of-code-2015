import time


def contains_twice_char_no_overlap(s):
    for i in range(len(s) - 1):
        pair = s[i] + s[i + 1]
        temp = s[:i] + '--' + s[i + 2:]

        if pair in temp:
            return True

    return False


def contains_one_letter_between(s):
    for i in range(len(s) - 2):
        if s[i] == s[i + 2]:
            return True

    return False


def is_nice(s):
    return (contains_twice_char_no_overlap(s)
            and contains_one_letter_between(s))


def main():
    inputs = standard_func.get_input_as_str('input.txt')
    # inputs = ['xilodxfuxphuiiii']
    nice_count = 0

    for input in inputs:
        if is_nice(input):
            print(input)
            nice_count += 1

    print(nice_count)


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
