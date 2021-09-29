### Task 4.5
# Implement a decorator `remember_result` which remembers last result of function it decorates and prints it before next call.
# ```python
# @remember_result
# def sum_list(*args):
# 	 result = ""
#	 for item in args:
#		 result += item
#	 print(f"Current result = '{result}'")
#	 return result

# sum_list("a", "b")
# >>> "Last result = 'None'"
# >>> "Current result = 'ab'"
# sum_list("abc", "cde")
# >>> "Last result = 'ab'" 
# >>> "Current result = 'abccde'"
# sum_list(3, 4, 5)
# >>> "Last result = 'abccde'" 
# >>> "Current result = '12'"
#```

prev_result = None

def check_if_it_int (*args):
    for unit in args:
        type_of_int = (isinstance(unit, int))
    return type_of_int

def remember_result(sum_list):
    def prev_result(*args):
        global prev_result 
        print(f"Last result = '{prev_result}'")   
        current_result = sum_list(*args)
        prev_result = str(current_result)
    return prev_result

@remember_result
def sum_list(*args):
    if check_if_it_int (*args) == False:
        result = ""
    else:
        result = 0

    for item in args:
        result += item
    print(f"Current result = '{result}'")
    return result

sum_list("a", "b")
sum_list("abc", "cde")
sum_list(3, 4, 5)