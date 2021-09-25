### Task 4.9
# Implement a bunch of functions which receive a changeable number of strings and return next parameters:
# 1) characters that appear in all strings
# 2) characters that appear in at least one string
# 3) characters that appear at least in two strings
# 4) characters of alphabet, that were not used in any string

# Note: use `string.ascii_lowercase` for list of alphabet letters

#```python
# test_strings = ["hello", "world", "python", ]
# print(test_1_1(*strings))
# >>> {'o'}
# print(test_1_2(*strings))
# >>> {'d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y'}
# print(test_1_3(*strings))
# >>> {'h', 'l', 'o'}
# print(test_1_4(*strings))
# >>> {'a', 'b', 'c', 'f', 'g', 'i', 'j', 'k', 'm', 'q', 's', 'u', 'v', 'x', 'z'}
#```

import string

############################################### ugly functions lives here )))
def all_char_in_lst(inp_str_lst: list): # forming char sets grouped by str
    all_str_lst = []
    one_word_char = []
    for i in range(len(inp_str_lst)):
        for ch in inp_str_lst[i]:
            if ch not in one_word_char:
                one_word_char.append(ch)          
        all_str_lst.append(one_word_char)
        one_word_char = []
    return all_str_lst

def let_it_dict (inp_list_for_dict: list):  # forming of a dictionary w the n of entries
    test_strings = inp_to_list(*strings)
    dict_of_char = {}
    inp_list_for_dict = test_1_2(inp_list_for_dict)
    for ch_key in inp_list_for_dict:  # fill in w zeros f further calc
        dict_of_char[ch_key] = int(0)
    for ch_key in all_char_in_lst(test_strings): # ext unique char w break by str
        for ch in ch_key:     
             if ch in dict_of_char: # running char calc entries in str 
                dict_of_char[ch] = int(str(dict_of_char[ch])) + 1
    return dict_of_char

def entry_counter (test_str: list, min_entry_counter = 2 ): # default value of entr=2 for sub.task 3
    out_list = []
    for key, value in let_it_dict(test_str).items():
        if value >= min_entry_counter:
            out_list.append(key)
    return out_list

def inp_to_list(*args):
    output = []
    for wrd in args:
        output.append(wrd)
    return output
###############################################
    
def test_1_1(*strings): 
    test_strings = inp_to_list(*strings)
    return entry_counter(test_strings, len(all_char_in_lst(test_strings)))

def test_1_2(*test_str): # all unique char - will use later
    if  isinstance(test_str, tuple):
        test_str = inp_to_list(*strings)
    else:
        test_str = list(test_str)
    str_of_1_wrds = []
    for i in range(len(test_str)):
        for ch in test_str[i]:
            if ch not in str_of_1_wrds:
                str_of_1_wrds.append(ch)
    str_of_1_wrds = sorted(str_of_1_wrds)
    return str_of_1_wrds

def test_1_3(*strings):
    test_strings = inp_to_list(*strings)
    return entry_counter(test_strings)    

def test_1_4(*strings): 
    test_strings = inp_to_list(*strings)
    unused_alph = []
    alph = string.ascii_lowercase
    for ch in alph:
        if ch not in (test_1_2(test_strings)):
            unused_alph.append(ch)
    unused_alph = sorted(unused_alph)
    return unused_alph

strings = ["hello", "world", "python", ]

print(test_1_1(*strings))
print(test_1_2(*strings))
print(test_1_3(*strings))
print(test_1_4(*strings))