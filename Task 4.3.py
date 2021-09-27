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