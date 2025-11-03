
for num in range(10):
    for i in range(num):
        print(i, end=" ")
    print("\n")
    
# palindrome
num =  input("Enter a nmber: ")
if(num[::-1] == num):
    print("Num is a palindrome")
else:
    print("false")
    
    
