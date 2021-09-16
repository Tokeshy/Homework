### Task 1.5
#Write a Python program to print all unique values of all dictionaries in a list.
#Examples:
#Input: [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
#Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
Def_list = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
Uni_val_set = []
for Inner_unit in Def_list:
    for key, value in Inner_unit.items():
        if value not in Uni_val_set:
            Uni_val_set.append(value) 
print(Uni_val_set)
