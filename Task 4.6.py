### Task 4.6
# Implement a function `get_shortest_word(s: str) -> str` which returns the
# longest word in the given string. The word can contain any symbols except
# whitespaces (` `, `\n`, `\t` and so on). If there are multiple longest words in
# the string with a same length return the word that occures first.
# Example:
# ```python
#  >>> get_shortest_word('Python is simple and effective!')
# 'effective!'

#  >>> get_shortest_word('Any pythonista like namespaces a lot.')
# 'pythonista'
# ```

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
