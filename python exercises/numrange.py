# use end='' or end=' ' to print on the same line
n = int(input("Enter the number you want to print: "))
if n >= 1 and n <= 150:
    for num in range(1,n+1):
        print(num, end='')
elif n <= 0 :
    print("negative values")
else:
    print("Out of range")