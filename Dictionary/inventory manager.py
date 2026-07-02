# Create an inventory manager that stores items and their quantities using a dictionary.

items = {}


def shop():
    while True:
        ch = input("\n1.Add 2.Check 3.Exit : ")

        if ch == "1":
            items[input("Item: ")] = int(input("Quantity: "))
        elif ch == "2":
            print(items.get(input("Item: "), "Not Found"))
        else:
            break


shop()