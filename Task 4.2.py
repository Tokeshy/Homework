### Task 4.2
# Implement a function which search for most common words in the file.
# Use `data/lorem_ipsum.txt` file as a example.

#```python
#def most_common_words(filepath, number_of_words=3):
#    pass
#print(most_common_words('lorem_ipsum.txt'))
#>>> ['donec', 'etiam', 'aliquam']
#```
#> NOTE: Remember about dots, commas, capital letters etc.

import string

file_load_path = 'D:\\_Git\\EpamPythonTraining\\Homework\\data\\lorem_ipsum.txt'

def most_common_words(filepath, number_of_words=3):
    letters = string.ascii_lowercase
    lines = []
    words_counter = {}
    out_list = []
    with open(filepath, 'r') as loaded_file:
        for line in loaded_file:
            lines.append(line.strip().lower().split(' '))
    loaded_file.close

    for line in lines:
        for word in line:
            new_word = ''
            for ch in word:
                if ch not in letters:
                    ch = ''
                new_word = new_word + ch

            if new_word not in words_counter:
                words_counter[new_word] = int(1)
            else:
                words_counter[new_word] = int(str(words_counter[new_word])) + 1

    max_count = max(words_counter.values())
    for i in range(number_of_words+1):
        curr_max = max_count - i
        for k, v in words_counter.items():
            if v == curr_max and len(out_list) < number_of_words and k != '':
                out_list.append(k)

    return out_list

print(most_common_words(file_load_path))
