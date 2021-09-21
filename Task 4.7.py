### Task 4.7
# Implement a function `foo(List[int]) -> List[int]` which, given a list of
# integers, return a new list such that each element at index `i` of the new list
# is the product of all the numbers in the original array except the one at `i`.
# Example:
# ```python
# >>> foo([1, 2, 3, 4, 5])
# [120, 60, 40, 30, 24]

# >>> foo([3, 2, 1])
# [2, 3, 6]
# ```

def foo(list_to_product: list):
    output_list = ()
    output_list = list(output_list) 
    temp_list = list_to_product
    



    for i in range(len(list_to_product)):
        temp_list = list_to_product
        #print(i)
        #temp_list = temp_list.pop[i] #= 
        #del temp_list[len(temp_list)-i]
        print(temp_list)
        print('-----------------')
        #print(temp_list)
  #      multipl_numb = 1
  #      for numb in temp_list:
  #          multipl_numb *= int(numb)
  #         output_list.append(int(multipl_numb)) 
        
   # for i in range (len(list_to_product)):
        #multipl_numb = 1
        #temp_list = list_to_product 

        #del temp_list[i]
        ###print ('@@@@@@@@@')
        ####print(temp_list)



        #if len(temp_list) >= i:
        #    del temp_list[i]
        #for numb in temp_list:
        #    multipl_numb = int(multipl_numb) * int(numb)
        #    output_list.append(int(multipl_numb))

    return output_list

#foo([3, 2, 1])
temp_list = [3, 2, 1]
temp_list_a = temp_list
temp_list_b = temp_list

del temp_list_a[2]
del temp_list_b[1]

print(temp_list_a)
print(temp_list_b)
#tmp = [3, 2, 1]
#del tmp[2]
#print(tmp)