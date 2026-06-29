# Check if the elements in the first half of the tuple are sorted in ascending order

def sort(tup):
    ln = len(tup)
    mid = ln // 2

    if ln % 2 == 1:
        mid = mid + 1

    half = tup[:mid]

    if sorted(half) == list(half):
        return "First half is sorted"
    else:
        return "First half is not sorted"


user = eval(input("Enter a tuple : "))
print(sort(user))