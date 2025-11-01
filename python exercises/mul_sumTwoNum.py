
# Given two integer numbers, write a Python program to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

def mul_sum(number1,number2):
   
   product = number1 * number2

   if(product <= 1000):
    return number1 * number2
   else:
    return number1 + number2


print(mul_sum(20,30))

