sales_data = [
    {"order_id": 1, "amount": 25.50, "status": "completed"},
    {"order_id": 2, "amount": 15.00, "status": "refunded"},
    {"order_id": 3, "amount": 120.00, "status": "completed"},
    {"order_id": 4, "amount": 8.99, "status": "completed"},
    {"order_id": 5, "amount": 45.00, "status": "refunded"}
]

# Task 1: List Comprehension
def get_completed_orders(sales):
    """Returns a new list containing ONLY the dictionaries where status is 'completed'."""
    completed_orders = [sale for sale in sales if sale['status'] == 'completed']
    return completed_orders

# Task 2: Lambda Functions
def sort_by_amount(sales):
    """Returns the list of sales sorted by the 'amount' key, from highest to lowest."""
    list_of_sales = sorted(sales, key=lambda x: x['amount'], reverse=True)
    return list_of_sales

# Task 3: *args
def calculate_total_revenue(*amounts):
    """Takes in any number of float amounts and returns the total sum."""
    return sum(amounts)


# --- Testing the Functions ---
print("--- Completed Orders ---")
completed = get_completed_orders(sales_data)
for order in completed:
    print(order)

print("\n--- Sorted by Amount ---")
sorted_sales = sort_by_amount(sales_data)
for order in sorted_sales:
    print(order)

print("\n--- Total Revenue ---")
just_the_amounts = [sale['amount'] for sale in get_completed_orders(sales_data)]
total = calculate_total_revenue(*just_the_amounts) 
print(f"Total Revenue from completed sales: ${total:.2f}")