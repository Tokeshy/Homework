# Python Practice - Session 1

### Task 1.1
# Write a Python program to calculate the length of a string without using the `len` function.
Some_enteredString = input(str())
cn = 0
for ch in Some_enteredString:
    cn += 1
print(str(cn))

#################################################################
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

#################################################################
### Task 1.3
#Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form.
#Examples:
#Input: ['red', 'white', 'black', 'red', 'green', 'black']
#Output: ['black', 'green', 'red', 'white', 'red']
Inp_list = str(input()).split(',')
Out_list = []
for wrd in Inp_list: 
    wrd = wrd.replace(' ','')
    wrd.lower     
    if wrd not in Out_list:
        Out_list.append(wrd)
print(sorted(Out_list))

#################################################################
### Task 1.3
#Create a program that asks the user for a number and then prints out a list of all the [divisors](https://en.wikipedia.org/wiki/Divisor) of that number.
#Examples:
#Input: 60
#Output: {1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60}
import math # unwritten code is the best so i decided do not to "reinvent the wheel"

def divisorGenerator(n): 
    List_of_divs = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                List_of_divs.append(int(n / i))
    for divisor in reversed(List_of_divs):
        yield divisor

Numb_to_check = int(input())
print (list(divisorGenerator(Numb_to_check)))

#################################################################
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

#################################################################
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

#################################################################
### Task 1.6
#Write a Python program to convert a given tuple of positive integers into an integer. 
#Examples:
#Input: (1, 2, 3, 4)
#Output: 1234
Inp_tup = (1, 2, 3, 4)
Int_in_str = ''
Int_in_int = 0
for n in Inp_tup:
    Int_in_str += str(n)
Int_in_int = int(Int_in_str)
print(Int_in_int)

#################################################################
### Task 1.6
#Write a program which makes a pretty print of a part of the multiplication table.
#Examples:
#Input:
#a = 2
#b = 4
#c = 3
#d = 7
#Output:
#	3	4	5	6	7	
#2	6	8	10	12	14	
#3	9	12	15	18	21	
#4	12	16	20	24	28
def GetInt (nstr): # let's clean input & convert it into int
    nstr = nstr.replace(' ','')
    nint = int(nstr[nstr.index('=') + 1: len(nstr)])
    return nint

a = GetInt(input())
b = GetInt(input())
c = GetInt(input())
d = GetInt(input())
ln = ''
ln1 = '   '
i = c
j = c

while i >= c and i <= d: # generation of 1st line
    ln1 = ln1 + '  ' + str(i)
    i+=1
print(ln1)    
i = a

while i >= a and i <= b: # the principle of generating subsequent lines is the same, so we just loop 
    ln = ln +'  ' + str(i)   
    while j >= c and j <= d:
        ln = ln + '  ' + str(j*i)
        j +=1
    print(ln)
    i += 1
    ln = ''
    j = c

#################################################################
### Materials
#* [Python Data Types](https://realpython.com/python-data-types/)
#* [Python Data Structures](https://realpython.com/python-data-structures/)
#* [Conditional Statements](https://realpython.com/python-conditional-statements/)
#* [While loop](https://realpython.com/python-while-loop/)
#* [For loop](https://realpython.com/python-for-loop/)
#* [Operators](http://pythonicway.com/python-operators)