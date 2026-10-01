MONTHS_IN_YEAR = 12
PERCENT_CONVERSION = 100

while (monthly_investment := float(input("Enter a monthly investment amount: "))) <= 0:
    print("Error: investment must be a positive number")

while (yearly_interest_rate := float(input("Enter a yearly interest rate: "))) <= 0:
    print("Error: yearly interest rate must be a positive number")

while (investment_years := int(input("Enter how many years to invest: "))) <= 0:
    print("Error: investment period must be a positive number of years")

monthly_rate = (yearly_interest_rate / PERCENT_CONVERSION) / MONTHS_IN_YEAR
total_months = investment_years * MONTHS_IN_YEAR
total_balance = 0.0

for month in range(1, total_months + 1):
    total_balance = (total_balance + monthly_investment) * (1 + monthly_rate)
    print(f"Month {month} revenue: {total_balance}")

print(f"\nAfter {investment_years} years, you will receive a total investment revenue of {total_balance:,.2f} at a yearly rate of {yearly_interest_rate}")