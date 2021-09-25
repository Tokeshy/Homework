# Python Practice - Session 4

##################################################################
### Task 4.1
# Implement a function which receives a string and replaces all `"` symbols
# with `'` and vise versa.
def Replacer (in_str):
    out_str = ''
    for ch in in_str:
        if ch == '"' :
            ch = "'"
        elif ch == "'":
            ch = '"' 
        out_str = out_str + ch
    return out_str

inp_str = input()
print(Replacer(inp_str))

##################################################################
### Task 4.2
# Write a function that check whether a string is a palindrome or not. Usage of
# any reversing functions is prohibited. To check your implementation you can use
# strings from [here](https://en.wikipedia.org/wiki/Palindrome#Famous_palindromes).
def is_this_palindrome (str_to_check):
    reg_str = ''
    rev_str = ''
    len_of_str = 0
    for ch in str_to_check:
        reg_str = reg_str + ch
        len_of_str += 1         # as we shouldn't use any func - let's calculate manually
    for i in range (len_of_str):
        rev_ch = str_to_check[len_of_str - i - 1]
        rev_str = rev_str + rev_ch

    if reg_str == rev_str:
        return 'is palindrome'
    else:
        return 'is not palindrome'

mayby_palindrom = "sator arepo tenet opera rotas" # please enter only lower case and no spaces in end, line beggin and between words 
                                                  # othercase "а роза упала на лапу азора" will work unexpectedly )))
print(is_this_palindrome(mayby_palindrom))

##################################################################
### Task 4.3
# Implement a function which works the same as `str.split` method
# (without using `str.split` itself, ofcourse).
def let_it_split (some_in_str, split_separator = ' '):
    if some_in_str[len(some_in_str) -1] != split_separator: # cause you never know what will the separator
        some_in_str += split_separator

    splited = []
    word_by_separator = ''
    for ch in some_in_str:
        if ch != split_separator:
           word_by_separator = word_by_separator + ch
        else:
            splited.append(word_by_separator) 
            word_by_separator = ''
    return splited

test_xt = "welcome to the jungle"

print(let_it_split(test_xt))

# and also some test spam
print(' ## ## ## ## ## ')
print(let_it_split(test_xt, 'o'))
print(' ## ## ## ## ## ')
print(let_it_split(test_xt, ' '))
print(' ## ## ## ## ## ')

##################################################################
### Task 4.4
#Implement a function `split_by_index(s: str, indexes: List[int]) -> List[str]`
#which splits the `s` string by indexes specified in `indexes`. Wrong indexes
#must be ignored.
#Examples:
#```python
#>>> split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])
#["python", "is", "cool", ",", "isn't", "it?"]

#>>> split_by_index("no luck", [42])
#["no luck"]
#```
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

##################################################################
### Task 4.5
#Implement a function `get_digits(num: int) -> Tuple[int]` which returns a tuple
#of a given integer's digits.
#Example:
#```python
#>>> split_by_index(87178291199)
#(8, 7, 1, 7, 8, 2, 9, 1, 1, 9, 9)
#```
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

##################################################################
### Task 4.6
#Implement a function `get_shortest_word(s: str) -> str` which returns the
#longest word in the given string. The word can contain any symbols except
#whitespaces (` `, `\n`, `\t` and so on). If there are multiple longest words in
#the string with a same length return the word that occures first.
#Example:
#```python

#>>> get_shortest_word('Python is simple and effective!')
#'effective!'

#>>> get_shortest_word('Any pythonista like namespaces a lot.')
#'pythonista'
#```
def get_shortest_word(s: str):  #so why 'get_shortest' if 'longest' one ??
    longest_one = ''
    word = ''
    s += ' ' # if the white spaces is ours separator
    for ch in s:
        if ch != ' ':
           word = word + ch
        elif ch == ' ':
            if len(longest_one) < len(word):
                longest_one = word
            word = ''
    return longest_one

some_enterd_str_A = 'Python is simple and effective!'
some_enterd_str_B = 'Any pythonista like namespaces a lot.'

print(get_shortest_word(some_enterd_str_A))
print(get_shortest_word(some_enterd_str_B))

##################################################################
### Task 4.7
#Implement a function `foo(List[int]) -> List[int]` which, given a list of
#integers, return a new list such that each element at index `i` of the new list
#is the product of all the numbers in the original array except the one at `i`.
#Example:
#```python
#>>> foo([1, 2, 3, 4, 5])
#[120, 60, 40, 30, 24]

#>>> foo([3, 2, 1])
#[2, 3, 6]
#```
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

##################################################################
### Task 4.8
#Implement a function `get_pairs(lst: List) -> List[Tuple]` which returns a list
#of tuples containing pairs of elements. Pairs should be formed as in the
#example. If there is only one element in the list return `None` instead.
#Example:
#```python
#>>> get_pairs([1, 2, 3, 8, 9])
#[(1, 2), (2, 3), (3, 8), (8, 9)]

#>>> get_pairs(['need', 'to', 'sleep', 'more'])
#[('need', 'to'), ('to', 'sleep'), ('sleep', 'more')]

#>>> get_pairs([1])
#None
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

##################################################################
### Task 4.9
# Implement a bunch of functions which receive a changeable number of strings and return next parameters:
# 1) characters that appear in all strings
# 2) characters that appear in at least one string
# 3) characters that appear at least in two strings
# 4) characters of alphabet, that were not used in any string

# Note: use `string.ascii_lowercase` for list of alphabet letters

#```python
#test_strings = ["hello", "world", "python", ]
#print(test_1_1(*strings))
#>>> {'o'}
#print(test_1_2(*strings))
#>>> {'d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y'}
#print(test_1_3(*strings))
#>>> {'h', 'l', 'o'}
#print(test_1_4(*strings))
#>>> {'a', 'b', 'c', 'f', 'g', 'i', 'j', 'k', 'm', 'q', 's', 'u', 'v', 'x', 'z'}
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

def entry_counter (test_str: list, min_entry_counter = 2 ): # def val of entr=2 for sub.task 3
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

##################################################################
### Task 4.10
#Implement a function that takes a number as an argument and returns a dictionary, where the key is a number and the value is the square of that number.
#```python
#print(generate_squares(5))
#>>> {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
#```
def generate_squares(lim_numb: int):
    out_dict = {}
    for i in range (1, lim_numb + 1):
        out_dict[i] = i*i
    return out_dict

print(generate_squares(5))

##################################################################
### Task 4.11
#Implement a function, that receives changeable number of dictionaries (keys - letters, values - numbers) and combines them into one dictionary.
#Dict values ​​should be summarized in case of identical keys

#```python
#def combine_dicts(*args):
#    ...

#dict_1 = {'a': 100, 'b': 200}
#dict_2 = {'a': 200, 'c': 300}
#dict_3 = {'a': 300, 'd': 100}

#print(combine_dicts(dict_1, dict_2)
#>>> {'a': 300, 'b': 200, 'c': 300}

#print(combine_dicts(dict_1, dict_2, dict_3)
#>>> {'a': 600, 'b': 200, 'c': 300, 'd': 100}
#```
def combine_dicts(*args):
    combined_dict = {}
    for temp_dict in args:
        for key in temp_dict:
            if key in combined_dict:
                combined_dict[key] = int(combined_dict[key]) + int(temp_dict[key])
            else:
                combined_dict[key] = int(temp_dict[key]) 
    return combined_dict


dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}

print(combine_dicts(dict_1, dict_2))
print(combine_dicts(dict_1, dict_2, dict_3))

### Materials
#* [Scope](https://python-scripts.com/scope)
#* [Functions](https://python-scripts.com/functions-python)
#* [Defining your own python function](https://realpython.com/defining-your-own-python-function/)
#* [Python Lambda](https://realpython.com/python-lambda/)