### Task 1.2
# Write a Python program to count the number of characters (character frequency) in a string (ignore case of letters).
# Examples:
# Input: 'Oh, it is python' 
# Output: {',': 1, ' ': 3, 'o': 2, 'h': 2, 'i': 2, 't': 2, 's': 1, 'p': 1, 'y': 1, 'n': 1}
Inp_str = input(str().lower)
ch_set = {}
for ch in Inp_str:
    if ch not in ch_set:
        ch_set[ch] = 1
    else:
        ch_set[ch] = ch_set[ch] + 1
print(ch_set)