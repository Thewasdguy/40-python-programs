# Question: Accepts a list of 10 positive and negative integers. Write a function to create two separate lists: one for negative numbers and another for positive numbers. Display both lists side-by-side.

def separate_negatives(mixed_list):
    pos_list = []
    neg_list = []
    
    for num in mixed_list:
        if num >= 0:
            pos_list.append(num)
        else:
            neg_list.append(num)
            
    print("Positive numbers list:", pos_list)
    print("Negative numbers list:", neg_list)

# orgasm
data_list = [15, -3, 0, 42, -9, -1, 88, 12, -7, 5]
print("Original mixed list:", data_list)

separate_negatives(data_list)
