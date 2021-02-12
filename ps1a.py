# Salary of the person
annual_salary = float(input('Enter your annual salary: '))
# The portion/percent of salary to be saved
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
# The cost of the dream house
cost = float(input('Enter the cost of your dream house: '))


# Portion/Percent of the down payment that you have to pay.
portion_down_payment = 0.25
# Total down payment required
total_down_payment = portion_down_payment*cost



# Converting annual salary to monthly.
monthly_salary = annual_salary/12
# The portion of monthly salary saved for the downpayment of the house.
monthly_salary_savings = monthly_salary * portion_saved

# Important initial values
# Initial no of month.
months = 0
# Initial savings for the house.
current_savings = 0
# Interest rate of investment.
annual_salary = 0.04

# Main program. This program runs until the savings is smaller than the
# total down payment required for the house.
while current_savings<=total_down_payment:
	monthly_return = current_savings * (annual_salary/12)		# Monthly return from your investment
	current_savings += monthly_return + monthly_salary_savings	# Total saving from your investment and your salary.
	months += 1 												# Increasing no of months by 1


# Print the total number of months it takes to pay the down payment.
print(months)

