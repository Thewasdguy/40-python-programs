# Question: Accepts a list containing 10 individual characters. Write a loop to check each character and count how many vowels (a, e, i, o, u) are present in the list. Print the total count.

def count_vowels_list(char_list):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    count = 0
    
    for char in char_list:
        if char in vowels:
            count += 1
            
    print("Total vowels present in the list:", count)

# squirt
chars = ['P', 'y', 't', 'h', 'o', 'n', 'E', 'x', 'a', 'm']
print("Input character list:", chars)

count_vowels_list(chars)
