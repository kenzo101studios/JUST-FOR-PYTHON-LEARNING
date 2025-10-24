# ☕ Coffee Shop v2
# Based on lessons from NetworkChuck + your own improvements :)

print("Welcome to The Python Coffee Shop!\n")

# --- MENU ---
menu = {
    "espresso": 4,
    "latte": 5,
    "cappuccino": 5,
    "frappuccino": 6,
    "tea": 3,
    "coffee": 4,
    "hot chocolate": 5,
    "water": 2
}

# --- START ---
name = input("What is your name? \n> ").title()
print(f"\nHello {name}! Here’s our menu:\n")

# Display menu dynamically
for drink, price in menu.items():
    print(f" - {drink.title()} : ${price}")

# --- ORDER LOOP ---
order_list = []
total = 0

while True:
    order = input(
        "\nWhat would you like to order? (type 'done' to finish)\n> ").lower()

    if order == "done":
        break

    if order not in menu:
        print("❌ Sorry, we don’t have that item. Please choose from the menu.")
        continue

    try:
        quantity = int(input(f"How many {order.title()} would you like?\n> "))
        if quantity <= 0:
            print("Please enter a positive number.")
            continue
    except ValueError:
        print("⚠️ That’s not a number. Try again.")
        continue

    # Calculate and record the order
    cost = menu[order] * quantity
    total += cost
    order_list.append((order, quantity, cost))

    print(f"✅ Added {quantity} x {order.title()} (${cost}) to your order.")

# --- RECEIPT ---
print("\n-----------------------------")
print("         ☕ RECEIPT ☕")
print("-----------------------------")
for item, qty, cost in order_list:
    print(f"{item.title()} x{qty}  -  ${cost}")
print("-----------------------------")
print(f"TOTAL: ${total}")
print("-----------------------------")

print(
    f"\nThank you, {name}! Your drinks will be ready soon. Have a great day! 🌟"
)
