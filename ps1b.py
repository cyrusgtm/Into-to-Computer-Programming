# Salary of the person
annual_salary = float(input('Enter your annual salary: '))
# The portion of salary to be saved
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
# The cost of your dream house
cost = float(input('Enter the cost of your dream house: '))
# The semi-annual salary raise
semi_annual_raise = float(input('Enter the semi annual salary raise: '))

# annual_salary = 120000
# portion_saved = 0.05
# cost = 500000
# semi_annual_raise = 0.03


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
annual_return = 0.04

# Main program. This program runs until the saving is smaller than the
# total down payment required for the house. Since the monthly salary is increases
# semiannually the savings also increase which is accounted by the if statement. 
while current_savings<=total_down_payment:
	months += 1													# Increasing number of months
	monthly_return = current_savings * (annual_return/12)		# Monthly return from your investment
	current_savings += monthly_return + monthly_salary_savings	# Total saving from your investment and your salary. 
	if months % 6 == 0 :										# Checking the 6th month.  
		monthly_salary += semi_annual_raise*monthly_salary 		# Increasing the monthly salary
		monthly_salary_savings = monthly_salary * portion_saved # Increasing the savings with respect to the salary increase.
			
# Print the total number of months it takes to pay the down payment.															
print(months)

		





