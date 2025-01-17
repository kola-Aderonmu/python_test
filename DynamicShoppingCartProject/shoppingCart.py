# Shopping cart program in Python

def add_to_cart(cart, item_name, price, *args, **kwargs):
    """
    Adds an item to the shopping cart.

    Arguments:
    - cart: The shopping cart (a list of dictionaries).
    - item_name: The name of the item to add.
    - price: The price of the item.
    - *args: Optional discounts (percentage values like 10, 20, etc.).
    - **kwargs: Optional details about the item (e.g., color, size).
    """
    # Check if the item already exists in the cart
    for item in cart:
        if item['name'] == item_name:
            print(f"{item_name} is already in the cart. Skipping duplicate.")
            return cart  # Do not add duplicates

    # Calculate the final price after applying discounts
    final_price = price
    for discount in args:
        # Apply each discount sequentially
        final_price -= final_price * (discount / 100)

    # Create the item dictionary
    item = {
        'name': item_name,
        'price': price,
        'final_price': round(final_price, 2),  # Round to 2 decimal places
        'details': kwargs
    }

    # Add the item to the cart
    cart.append(item)
    details_str = ", ".join(f"{key}={value}" for key, value in kwargs.items())
    print(f"Item added: {item_name} - Final Price: ${round(final_price, 2)} ({details_str})")

    return cart

def display_cart(cart):
    """
    Displays the contents of the shopping cart and the total cost.

    Arguments:
    - cart: The shopping cart (a list of dictionaries).
    """
    print("\n--- Cart Summary ---")
    total_cost = 0

    # Loop through each item in the cart
    for item in cart:
        details = ", ".join(f"{key}={value}" for key, value in item['details'].items())
        print(f"{item['name']} - ${item['final_price']} ({details})")

        # Accumulate the total cost
        total_cost += item['final_price']

    print(f"\nTotal Cost: ${round(total_cost, 2)}")

# Initialize an empty cart
shopping_cart = []

while True:
    # Prompt the user to add an item to the cart
    item_name = input("Enter item name (or 'done' to finish): ").strip()

    if item_name.lower() == 'done':
        break  # Exit the loop when the user is done adding items

    try:
        # Get the price of the item
        price = float(input("Enter item price: "))

        # Get optional discounts
        discounts = input("Enter discounts (if any, separated by spaces): ").strip()
        if discounts:
            discounts = [float(d) for d in discounts.split()]
        else:
            discounts = []

        # Get optional details
        details = {}
        item_details = input("Enter item details (e.g., color=red size=large): ").strip()
        if item_details:
            for detail in item_details.split():
                if "=" in detail:
                    key, value = detail.split("=")
                    details[key] = value
                else:
                    # Handle single-word details by assigning a default key (e.g., 'description')
                    details['description'] = detail

        # Add the item to the cart
        shopping_cart = add_to_cart(shopping_cart, item_name, price, *discounts, **details)

    except ValueError:
        print("Invalid input. Please try again.")

# Display the cart summary after exiting the loop
display_cart(shopping_cart)
