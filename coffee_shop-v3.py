# ☕ Coffee Shop v3
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


# --- RECEIPT CONTENT ---
receipt_lines = []
receipt_lines.append("\n-----------------------------")
receipt_lines.append("         ☕ RECEIPT ☕")
receipt_lines.append("-----------------------------")

for item, qty, cost in order_list:
    receipt_lines.append(f"{item.title()} x{qty}  -  ${cost}")

receipt_lines.append("-----------------------------")
receipt_lines.append(f"TOTAL: ${total}")
receipt_lines.append("-----------------------------")
receipt_lines.append(f"\nThank you, {name}! Your drinks will be ready soon. Have a great day! 🌟")

# --- PRINT RECEIPT TO SCREEN ---
print("\n".join(receipt_lines))

# --- SAVE RECEIPT TO FILE ---
filename = f"receipt_{name.replace(' ', '_')}.txt"

with open(filename, "w") as f:
    f.write(f"Customer: {name}\n")
    f.write("\n".join(receipt_lines))
    f.write("\n")

print(
    f"\nThank you, {name}! Your drinks will be ready soon. Have a great day! 🌟"
)

print(f"Oh. Also {name}, the Receipt has been saved to: {filename} \n")
