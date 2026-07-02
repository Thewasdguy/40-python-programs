# Count how many even and odd numbers the user enters.


def count():
    print("Question: Enter numbers and count how many are even or odd.")

    numbers = {}
    even = odd = 0

    n = int(input("How many numbers? "))
    for i in range(n):
        num = int(input("Enter number: "))
        numbers[i] = num

    for num in numbers.values():
        if num % 2 == 0:
            even += 1
        else:
            odd += 1

    print("Even numbers:", even)
    print("Odd numbers:", odd)


count()