import time


def contains_three_vowels(s):
    vowel_count = 0
    vowel_set = set(['a', 'e', 'i', 'o', 'u'])

    for char in s:
        if char in vowel_set:
            vowel_count += 1

    return True if vowel_count >= 3 else False


def contains_twice_char(s):
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return True
    
    return False


def is_naughty(s):
    bad_strings = ['ab', 'cd', 'pq', 'xy']

    for bad_string in bad_strings:
        if bad_string in s:
            return True

    return False


def is_nice(s):
    return (contains_three_vowels(s)
            and contains_twice_char(s)
            and not is_naughty(s))


def main():
    inputs = standard_func.get_input_as_str('input.txt')
    # inputs = standard_func.get_input_as_str('test.txt')
    
    nice_count = 0

    for input in inputs:
        if is_nice(input):
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
