### Task 1.4
#Write a Python program to sort a dictionary by key.
Def_dict = {1: 2, 3: 4, 2: 9, 4:8} # as ex
Sorted_dict = {}
Key_list = []
for key, value in Def_dict.items() :
    if key not in Key_list:
        Key_list.append(key)
for Sorted_key in sorted(Key_list):
    Sorted_dict[Sorted_key] = Def_dict[Sorted_key]
print(Sorted_dict) # as chk