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