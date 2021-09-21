### Task 4.4
# Implement a function `split_by_index(s: str, indexes: List[int]) -> List[str]`
# which splits the `s` string by indexes specified in `indexes`. Wrong indexes
# must be ignored.
# Examples:
#python
# >>> split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])
# ["python", "is", "cool", ",", "isn't", "it?"]

#>>> split_by_index("no luck", [42])
#["no luck"]

def split_by_index(s: str, indexes: list):
    out_list = []
    cutted_word = ''
    alt_ind = 0

    for is_index_ok in indexes: # check for indexes
        if is_index_ok >= len(s):
            return s
            break

    for i in range(len(s)): # if it's OK w index moving forward
        cutted_word = cutted_word + s[i]
        if i == int(indexes[alt_ind]-1):
            out_list.append(cutted_word)
            cutted_word = ''
            if alt_ind < len(indexes) - 1:
                alt_ind += 1
    return out_list    

print(split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]))
print(split_by_index("no luck", [42]))