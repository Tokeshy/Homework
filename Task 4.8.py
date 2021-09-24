### Task 4.8
# Implement a function `get_pairs(lst: List) -> List[Tuple]` which returns a list
# of tuples containing pairs of elements. Pairs should be formed as in the
# example. If there is only one element in the list return `None` instead.
# Example:
# ```python
# >>> get_pairs([1, 2, 3, 8, 9])
# [(1, 2), (2, 3), (3, 8), (8, 9)]

# >>> get_pairs(['need', 'to', 'sleep', 'more'])
# [('need', 'to'), ('to', 'sleep'), ('sleep', 'more')]

# >>> get_pairs([1])
# None
#```

def get_pairs(lst: list):
    out_list = []
    out_lst_unit = []
    if len(lst) == 1:
        out_list = None
    else:
        for i in range(0, len(lst)-1):
            out_lst_unit.append(lst[i])
            out_lst_unit.append(lst[i+1])
            out_list.append(tuple(out_lst_unit))
            out_lst_unit.clear()
    return out_list


print(get_pairs([1, 2, 3, 8, 9]))
print(get_pairs([1]))
