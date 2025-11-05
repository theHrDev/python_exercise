color_list = ["Red","Green","White" ,"Black"]
for color in color_list:
    fist_color = color_list[0]
    last_color = color_list[-1]
print("%s  %s" % (fist_color, last_color))


# Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.
def test_distinct(data):
    if(len(data)== len(set(data))): #Element in a set are expected to be unique
        return True
    else:
        return False
    
print(test_distinct([12,3,5,6,6,7])) 
print(test_distinct([12,3,5,6,7]))


# Write a Python function that identifies all pairs of numbers in a list that sum to a given value, ensuring each pair consists of unique numbers.
# def unique_to_sum(data,sum):
#     for num in set(data):
#         print(num)
#         if (num )

# will come back to this
