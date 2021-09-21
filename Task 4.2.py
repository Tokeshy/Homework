### Task 4.2
# Write a function that check whether a string is a palindrome or not. Usage of
# any reversing functions is prohibited. To check your implementation you can use
# strings from [here](https://en.wikipedia.org/wiki/Palindrome#Famous_palindromes).

def is_this_palindrome (str_to_check):
    reg_str = ''
    rev_str = ''
    len_of_str = 0
    for ch in str_to_check:
        reg_str = reg_str + ch
        len_of_str += 1         # as we shouldn't use any func - let's calculate manually
    for i in range (len_of_str):
        rev_ch = str_to_check[len_of_str - i - 1]
        rev_str = rev_str + rev_ch

    if reg_str == rev_str:
        return 'is palindrome'
    else:
        return 'is not palindrome'

mayby_palindrom = "sator arepo tenet opera rotas" # please enter only lower case and no spaces in end, line beggin and between words 
                                                  # othercase "а роза упала на лапу азора" will work unexpectedly )))
print(is_this_palindrome(mayby_palindrom))
