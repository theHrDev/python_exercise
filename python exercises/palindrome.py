def palindrome(number):
    if(number <= 9):
        return False
    else:
        reversed_num = str(number)[::-1]
    
    if(int(reversed_num) == number):
        return True
    else:
        return False
print(palindrome(12))
print(palindrome(121))
print(palindrome(2))
print(palindrome(0))