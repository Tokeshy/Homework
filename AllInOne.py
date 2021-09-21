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

##################################################################
### Task 4.9
#Implement a bunch of functions which receive a changeable number of strings and return next parameters:

#1) characters that appear in all strings

#2) characters that appear in at least one string

#3) characters that appear at least in two strings

#4) characters of alphabet, that were not used in any string

#Note: use `string.ascii_lowercase` for list of alphabet letters

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

##################################################################
### Task 4.10
#Implement a function that takes a number as an argument and returns a dictionary, where the key is a number and the value is the square of that number.
#```python
#print(generate_squares(5))
#>>> {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
#```

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

### Materials
#* [Scope](https://python-scripts.com/scope)
#* [Functions](https://python-scripts.com/functions-python)
#* [Defining your own python function](https://realpython.com/defining-your-own-python-function/)
#* [Python Lambda](https://realpython.com/python-lambda/)