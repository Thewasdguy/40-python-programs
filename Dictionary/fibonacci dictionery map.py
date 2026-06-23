fib = {0: 0, 1: 1}

def get_fibonacci(n):
    if n in fib:
        return fib[n]
    
    fib[n] = get_fibonacci(n - 1) + get_fibonacci(n - 2)
    return fib[n]

count = int(input("How many Fibonacci numbers do you want to generate?: "))

if count <= 0:
    print("Enter a number greater than 0.")
else:
    get_fibonacci(count - 1)
    
    print("Here is your Fibonacci numbers:")
    for position in range(count):
        print(f"{position} -> {fib[position]}")
