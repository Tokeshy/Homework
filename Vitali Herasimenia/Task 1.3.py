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