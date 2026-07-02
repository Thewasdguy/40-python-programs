# Count how many times each character appears in a string.

def count():
    print("Question: Enter a string and count the frequency of each character.")

    text = input("Enter a string: ")
    freq = {}

    for ch in text:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    print("Character Frequency:")
    print(freq)


count()