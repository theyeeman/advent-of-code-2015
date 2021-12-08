import time


def main():
    inputs = standard_func.get_input_as_str('input.txt')
    # inputs = standard_func.get_input_as_str('test.txt')
    temp = []
    
    for input in inputs:
        temp.append(input.split(' '))

    for t in temp:
        if len(t) == 3:
            print(t)


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

'''
brainstorming

what if i store each variable as a key in dict and value will be the expression that equals it?
    i.e. {c: 0
        b: p << 2
        p: j and x
        ...
    }

start with first entry in dict, and try to recursively evaluate?
    maybe i dont have to do it recursively, since in above example, i can just do b = my_dict[p] << 2 and this can turn into b = j and x << 2
    but how do i know when to stop?
        probably when there are no more variables in my string expression
        so will need to keep a separate dictionary to hold what ties into the
    just keep wrapping brackets around stuff?

trees are coming to mind...
    might need to build my own data structure
'''