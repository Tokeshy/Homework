### Task 4.6
# Implement a decorator `call_once` which runs a function or method once and caches the result.
# All consecutive calls to this function should return cached result no matter the arguments.
# ```python
# @call_once
# def sum_of_numbers(a, b):
#    return a + b

# print(sum_of_numbers(13, 42))
# >>> 55
# print(sum_of_numbers(999, 100))
# >>> 55
# print(sum_of_numbers(134, 412))
# >>> 55
# print(sum_of_numbers(856, 232))
# >>> 55
#```

is_first_run = True # indicator of first run

def call_once(func):  
    cashed_result = 0

    def check_for_prev_run (a, b):
        global is_first_run
        nonlocal cashed_result
        if is_first_run == True:
            cashed_result = func(a, b)
            is_first_run = False
        return cashed_result
    return check_for_prev_run

@call_once
def sum_of_numbers(a, b):
    return a + b

print(sum_of_numbers(13, 42))
print(sum_of_numbers(999, 100))
print(sum_of_numbers(134, 412))
print(sum_of_numbers(856, 232))