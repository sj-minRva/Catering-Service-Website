def calculate_tax(income):
    tax = 0  # Initialize tax to zero
    if income <= 250000:
        tax = 0
    elif income <= 500000:
        tax = (income - 250000) * 0.05
    elif income <= 1000000:
        tax = (income - 500000) * 0.2 + 250000 * 0.05
    else:
        tax = (income - 1000000) * 0.3 + 500000 * 0.2 + 250000 * 0.05
    return tax


try:
    print("...Calculating Income Tax...\n")
    
    # Get user input
    income = float(input("Enter your annual income (₹): "))
    
    # Calculate tax
    tax_amount = calculate_tax(income)
    
    # Display the calculated tax
    print(f"\nYour calculated tax is ₹{tax_amount:.2f}")

except ValueError:
    print("Invalid input! Please enter a numeric value.")
