# Question: Accepts a list of 10 product items. Write a loop to apply a 10% discount on all prices that are greater than ₹500. Modify the original list items directly and display the final values.

def update_prices(price_list):
    for i in range(len(price_list)):
        if price_list[i] > 500:
            discount = price_list[i] * 0.10
            price_list[i] = price_list[i] - discount
            
    print("Final discounted values:", price_list)

# Testing
prices = [200, 600, 450, 1200, 300, 800, 50, 550, 400, 1000]
print("Prices before discount:", prices)

update_prices(prices)
