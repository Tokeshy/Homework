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