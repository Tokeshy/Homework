### Task 4.5
# Implement a function `get_digits(num: int) -> Tuple[int]` which returns a tuple
# of a given integer's digits.
# Example:
# ```python
# >>> split_by_index(87178291199) # func name >> 'get_digits'
# (8, 7, 1, 7, 8, 2, 9, 1, 1, 9, 9)
# ```

def get_digits(num: int):
    output = ()
    str_num = str(num)
    for n in str_num:
        output = list(output) # is this kind of cheating ?
        output.append(int(n))
    output = tuple(output) # mean 'can i just write it here?'
    return (output)

some_entered_int = 87178291199
print(get_digits(some_entered_int))