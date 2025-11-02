# Write Python code to iterate through the 1 to 10 and, in each iteration, print the sum of the current and previous number.



def sum_cur_prev(num1,num2):
    previous_num = 0
    while num1 <= num2:
        sum = num1 + previous_num
        previous_num = num1
        print(f"The sum of previous num {previous_num} and the current num {num1} is {sum}")
        num1 += 1
    

sum_cur_prev(1,10)

# Another method
def curr_prev():
    previous_num = 0
    for num in range(10):
        sum = previous_num + num
        print(f"The sum of previous num {previous_num} and the current num {num} is {sum}")
        previous_num = num

curr_prev()

