# Question: Accepts a list of 10 elements. Shift every element one position to the left using a loop, making the first element move to the very end of the list. Return the shifted list.

def circular_left_shift(my_list):
    first_val = my_list[0]
    
    for i in range(len(my_list) - 1):
        my_list[i] = my_list[i + 1]
        
    my_list[-1] = first_val
    return my_list

# sex
elements = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("List before shifting:", elements)


shifted = circular_left_shift(elements)
print("List after circular left shift:", shifted)