def invest(amount, rate, years):
    """Calculates investment growth over time and prints the results."""
    print("\nInvestment Growth Over Time:")
    
    for year in range(1, years + 1):
        amount += amount * rate  # Increase by the annual rate
        print(f"Year {year}: ${amount:.2f}")

# Get user input
initial_amount = float(input("Enter the initial investment amount: "))
annual_rate = float(input("Enter the annual rate of return (as a percentage): ")) / 100
num_years = int(input("Enter the number of years: "))

# Call the function
invest(initial_amount, annual_rate, num_years)