def even_odd_checker():
    number = int(input("Enter a value: "))
    remainder = number % 2
    if(remainder == 0 ):
        return f"{number} is an even number"
    else:
        return f"{number} is an odd number"
    

print(even_odd_checker())



def list_odd_even():
    for num in range(10):
        if num % 2 == 0:
            print( f"{num} is an even number")
        else:
            print (f"{num} is an odd number")


list_odd_even()