# Function to calculate total items
def calculate_total(items):
  total = 0.0
  for item in items:
    total += item['price']
  return total

# Function to apply 10% discount if total exceed PHP 500.00
def apply_discount(total_amount):
  discount_rate = 0.1
  min_amount = 500.0

  if total_amount > min_amount:
    discount_amount = total_amount * discount_rate
    final_amount = total_amount - discount_amount
    return discount_amount, final_amount
  else:
    return 0.0, total_amount

# Function to display the receipt
def display_receipt(items, total_before_discount, discount_amount, final_amount):
  print("\n" + "="*30)
  print("        GROCERY RECEIPT")
  print("="*30)

  print("\nItems:")
  for item in items:
    # Using f-strings for formatted output
    print(f"- {item['name']}: ₱{item['price']:.2f}")

  print("-" * 30)
  print(f"Total Before Discount: ₱{total_before_discount:.2f}")

  if discount_amount > 0:
    print(f"Discount (10%):      - ₱{discount_amount:.2f}")
  else:
    print("Discount:            - ₱0.00")

  print("=" * 30)
  print(f"Final Amount to Pay: ₱{final_amount:.2f}")
  print("="*30 + "\n")

# Main function to collect input item name and item price three (3) times
def main():
  print("Welcome to the Mini Grocery Checkout!")
  items = []

  # Prompt user for 3 items
  for i in range(3):
    while True:
      item_name = input(f"Enter name of item {i+1}: ").strip()
      if item_name:
        break
      else:
        print("Item name cannot be empty. Please try again.")

    while True:
      try:
        item_price = float(input(f"Enter price of {item_name}: ₱"))
        if item_price >= 0:
          break
        else:
          print("Price cannot be negative. Please enter a valid price.")
      except ValueError:
        print("Invalid input. Please enter a numerical value for the price.")

    items.append({'name': item_name, 'price': item_price})

  # Calculate total
  total_before_discount = calculate_total(items)

  # Apply discount
  discount_amount, final_amount = apply_discount(total_before_discount)

  # Display receipt
  display_receipt(items, total_before_discount, discount_amount, final_amount)

if __name__ == "__main__":
    main()