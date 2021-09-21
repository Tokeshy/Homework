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