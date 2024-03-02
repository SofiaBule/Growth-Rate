# Calculate sales growth rate based on current and previous sales
def calculate_sales_growth_rate(current_sales, previous_sales):
    return ((current_sales - previous_sales) / previous_sales) * 100

# Example usage:
current_sales = 12000  # Current sales
previous_sales = 10000  # Previous sales
sales_growth_rate = calculate_sales_growth_rate(current_sales, previous_sales)
print("Sales growth rate:", sales_growth_rate, "%")
