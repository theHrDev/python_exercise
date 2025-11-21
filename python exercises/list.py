# From a list of integers, create two lists: even numbers and odd numbers.

num_list = [2,4,6,7,6,3,7,9]
even_list = []
odd_list = []
for num in num_list:
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)
        
print(odd_list)
print(even_list)
        