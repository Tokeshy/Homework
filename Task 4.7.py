### Task 4.7
# Implement a function `foo(List[int]) -> List[int]` which, given a list of
# integers, return a new list such that each element at index `i` of the new list
# is the product of all the numbers in the original array except the one at `i`.
# Example:
# ```python
# >>> foo([1, 2, 3, 4, 5])
# [120, 60, 40, 30, 24]

# >>> foo([3, 2, 1])
# [2, 3, 6]
# ```

def foo(list_to_product: list):
    list_to_product = tuple(list_to_product)
    output_list = []   
    for i in range(len(list_to_product)):
        temp_list = list(list_to_product)
        del temp_list[i]
        multipl_numb = 1
        for numb in temp_list:
            multipl_numb = multipl_numb * int(numb)

        output_list.append(multipl_numb)

    return output_list

temp_list_A = [1, 2, 3, 4, 5]
temp_list_B = [3, 2, 1]

print(foo(temp_list_A))
print(foo(temp_list_B))