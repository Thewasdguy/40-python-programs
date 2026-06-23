fib_cache = {0: 0, 1: 1}

def get_fibonacci(n):
    if n in fib_cache:
        return fib_cache[n]
    
    fib_cache[n] = get_fibonacci(n - 1) + get_fibonacci(n - 2)
    return fib_cache[n]

try:
    terms = int(input("Enter how many Fibonacci terms you want to generate: "))
    
    if terms <= 0:
        print("Please enter a positive integer greater than 0.")
    else:
        print("\nCalculating and storing terms...")
        get_fibonacci(terms - 1)
        print("\n--- Resulting Fibonacci Dictionary Map ---")
        print("{ Position : Fibonacci Number }")
        for position in sorted(fib_cache.keys()):
            if position < terms:
                print(f"Position {position:2d} -> {fib_cache[position]}")

except ValueError:
    print("Invalid input! Please enter a valid integer number.")