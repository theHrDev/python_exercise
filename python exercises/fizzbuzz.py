# 11. FizzBuzz
# Print numbers from 1 to 50:

# If divisible by 3 → print "Fizz"

# If divisible by 5 → print "Buzz"

# If divisible by both → print "FizzBuzz"

for num in range(51):
    if num % 3 == 0:
        print(f"{num} fizz")
    if num % 5 == 0:
        print(f"{num}  Buzz")
    if num % 3 == 0 and num % 5 == 0:
        print(f"{num} fizzBuzz")