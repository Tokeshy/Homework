# Python Practice - Session 4 // Homework 05


### Task 4.1
#Open file `data/unsorted_names.txt` in data folder. Sort the names and write them to a new file called `sorted_names.txt`. Each name should start with a new line as in the following example:
#```
#Adele
#Adrienne
#...
#Willodean
#Xavier
#```
file_load_path = 'D:\\_Git\\EpamPythonTraining\\Homework\\data\\unsorted_names.txt'
file_save_path = 'D:\\_Git\\EpamPythonTraining\\Homework\\data\\sorted_names.txt'

output_name_list = []
with open(file_load_path) as inp_name_list:
    for name_unit in inp_name_list:
        output_name_list.append(name_unit)
inp_name_list.close
output_name_list = sorted(output_name_list)

with open(file_save_path, 'w') as outp:
    for name_unit in output_name_list:
        outp.write(name_unit)
    outp.close

##################################################################
### Task 4.2
# Implement a function which search for most common words in the file.
# Use `data/lorem_ipsum.txt` file as a example.

#```python
# def most_common_words(filepath, number_of_words=3):
#    pass
# print(most_common_words('lorem_ipsum.txt'))
# >>> ['donec', 'etiam', 'aliquam']
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

##################################################################
### Task 4.3
# File `data/students.csv` stores information about students in [CSV](https://en.wikipedia.org/wiki/Comma-separated_values) format.
# This file contains the student’s names, age and average mark. 
# 1) Implement a function which receives file path and returns names of top performer students
# ```python
# def get_top_performers(file_path, number_of_top_students=5):
#    pass
# print(get_top_performers("students.csv"))
# >>> ['Teresa Jones', 'Richard Snider', 'Jessica Dubose', 'Heather Garcia', 'Joseph Head']
#```

#2) Implement a function which receives the file path with srudents info and writes CSV student information to the new file in descending order of age. 
#Result:
#``` 
#student name,age,average mark
#Verdell Crawford,30,8.86
#Brenda Silva,30,7.53
#...
#Lindsey Cummings,18,6.88
#Raymond Soileau,18,7.27
#```
file_load_path = 'D:\\_Git\\EpamPythonTraining\\Homework\\data\\students.csv'
file_folder = 'D:\\_Git\\EpamPythonTraining\\Homework\\data\\'

def file_loader(file_path):
    loaded_lines = []
    with open(file_path, 'r') as loaded_file:  #loading from scv, i not shure about is "import csv" forbidden/not so reinventing the circle
        for line in loaded_file:
            loaded_lines.append(line.strip().split(','))
    loaded_file.close 
    return loaded_lines 

def get_top_performers(file_path, number_of_top_students = 5): # Task 4.3.1
    student_rate = {}
    student_by_rate = []
    list_of_top = []

    loaded_lines = file_loader(file_path)

    for i in range(1, len(loaded_lines)):      # loading info into list for later sorting
        student_by_rate.append([float(loaded_lines[i][2]), loaded_lines[i][0]])  

    student_by_rate = sorted(student_by_rate)  # now it's sorted by rate, but i make a dict for you can check the output - sample output is not correct

    for i in range(len(student_by_rate) - 1, 1, -1):  # simply compiling output list
        student_rate[student_by_rate[i][1]] = student_by_rate[i][0]   
        if len(list_of_top) < number_of_top_students:
            list_of_top.append(student_by_rate[i][1])

    return list_of_top

def sort_by_age(file_path, new_file_name = 'students_by_age.csv'): # Task 4.3.2
    student_by_age = []
    out_list = []

    loaded_lines = file_loader(file_path)
    new_file = file_folder + new_file_name

    for i in range(1, len(loaded_lines)):      # loading info into list for later sorting
        student_by_age.append([int(loaded_lines[i][1]), loaded_lines[i][0], loaded_lines[i][2]])  

    student_by_age = sorted(student_by_age)
    out_list.append(loaded_lines[0][0] + ',' + loaded_lines[0][1] + ',' + loaded_lines[0][2])

    for i in range(len(student_by_age)-1, -1, -1):  # simply compiling output list
        out_list.append(str(student_by_age[i][1]) + ',' + str(student_by_age[i][0]) + ',' + str(student_by_age[i][2]))

    with open(new_file, 'w') as sorted_by_age:
        for line in out_list:
            sorted_by_age.write(str(line) + '\n')           
        sorted_by_age.close
    
    print('done, saved in ' + new_file_name)

print(get_top_performers(file_load_path))
sort_by_age(file_load_path)

##################################################################
### Task 4.4
#Look through file `modules/legb.py`.
#1) Find a way to call `inner_function` without moving it from inside of `enclosed_function`.
#2.1) Modify ONE LINE in `inner_function` to make it print variable 'a' from global scope.
#2.2) Modify ONE LINE in `inner_function` to make it print variable 'a' form enclosing function.

##################################################################
### Task 4.5
#Implement a decorator `remember_result` which remembers last result of function it decorates and prints it before next call.
#```python
#@remember_result
#def sum_list(*args):
#	result = ""
#	for item in args:
#		result += item
#	print(f"Current result = '{result}'")
#	return result

#sum_list("a", "b")
#>>> "Last result = 'None'"
#>>> "Current result = 'ab'"
#sum_list("abc", "cde")
#>>> "Last result = 'ab'" 
#>>> "Current result = 'abccde'"
#sum_list(3, 4, 5)
#>>> "Last result = 'abccde'" 
#>>> "Current result = '12'"
#```

##################################################################
### Task 4.6
#Implement a decorator `call_once` which runs a function or method once and caches the result.
#All consecutive calls to this function should return cached result no matter the arguments.
#```python
#@call_once
#def sum_of_numbers(a, b):
#    return a + b

#print(sum_of_numbers(13, 42))
#>>> 55
#print(sum_of_numbers(999, 100))
#>>> 55
#print(sum_of_numbers(134, 412))
#>>> 55
#print(sum_of_numbers(856, 232))
#>>> 55
#```

##################################################################
### Task 4.7*
#Run the module `modules/mod_a.py`. Check its result. Explain why does this happen.
#Try to change x to a list `[1,2,3]`. Explain the result.
#Try to change import to `from x import *` where x - module names. Explain the result. 


### Materials
#* [Decorators](https://realpython.com/primer-on-python-decorators/)
#* [Decorators in python](https://www.geeksforgeeks.org/decorators-in-python/)
#* [Python imports](https://pythonworld.ru/osnovy/rabota-s-modulyami-sozdanie-podklyuchenie-instrukciyami-import-i-from.html)
#* [Files in python](https://realpython.com/read-write-files-python/)
