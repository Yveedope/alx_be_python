# Prompt the user for their financial details
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Project annual savings with a fixed interest rate of 5%
annual_interest_rate = 0.05
projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * annual_interest_rate)

# Output results
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")
