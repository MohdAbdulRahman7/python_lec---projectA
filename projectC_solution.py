#Sample SOlution
# Ask kids to create a function to add items with their prices first and then users can use this system:

import math

# Item prices dictionary
item_prices = {
    'Apple': 1.50,
    'Banana': 0.50,
    'Milk': 2.00,
    'Eggs': 0.25
}

def calculate_total(items):
    """
    Calculate the total cost based on the shopping list.
    """
    total_cost = 0
    print("\nYou have bought:")
    for item, details in items.items():
        quantity, price = details
        item_cost = quantity * price
        total_cost += item_cost
        print(f"{quantity} {item}(s) - ${item_cost:.2f}")
    return total_cost

def main():
    print("Available items and prices:")
    for item, price in item_prices.items():
        print(f"{item} - ${price:.2f}")

    # Get user input
    num_items = int(input("\nHow many different items do you want to buy? "))
    shopping_list = {}

    for _ in range(num_items):
        item_name = input("Enter the name of the item: ").capitalize()
        if item_name in item_prices:
            quantity = int(input(f"How many {item_name}(s) do you want? "))
            shopping_list[item_name] = (quantity, item_prices[item_name])
        else:
            print(f"Sorry, {item_name} is not available. Please choose from the list.")

    # Calculate total
    total = calculate_total(shopping_list)
    print(f"\nTotal amount to pay: ${total:.2f}")
    print("Thank you for shopping at Walmart!")

if __name__ == "__main__":
    main()
