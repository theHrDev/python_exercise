# Write Python code to iterate through the 1 to 10 and, in each iteration, print the sum of the current and previous number.



def sum_cur_prev(num1,num2):
    previous_num = 0
    while num1 <= num2:
        sum = num1 + previous_num
        previous_num = num1
        print(f"The sum of previous num {previous_num} and the current num {num1} is {sum}")
        num1 += 1
    

sum_cur_prev(1,10)