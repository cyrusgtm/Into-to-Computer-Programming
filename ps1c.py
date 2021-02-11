# Salary of the person
annual_salary = float(input('Enter your annual salary: '))

# Semi annual raise
semi_annual_raise = 0.07
# Cost of the house
cost = 1000000


# Different monthly salary saving rates. This is initialized for the bisection search
# algorithm. Our goal is to search for a rate that  is between these two rates to find the most
# optimal set.
# The lowest rate of monthly salary saving possible
lower_rate = 0
# The highest rate of monthly salary saving possible 
higher_rate = 10000
# The margin of error
epsilon = 100
# Formula to calculate the monthly salary saving rate
guess_rate = (lower_rate + higher_rate)/2


# Portion/Percent of the down payment that you have to pay.
portion_down_payment = 0.25
# Total down payment required
total_down_payment = portion_down_payment*cost


# Converting annual salary to monthly. 
monthly_salary = annual_salary/12
# The portion of monthly salary saved for the downpayment of the house.
monthly_salary_savings = monthly_salary * guess_rate

portion_down_payment = 0.25
# Total down payment required
total_down_payment = portion_down_payment*cost


# Important initial values
current_savings = 0
# Interest rate of investment.
r = 0.04
# Initial steps in bisection
n = 0 

# Main program. This program runs until the difference between the savings and the total 
# down payment is below epsilon. 
while abs(current_savings - total_down_payment) >= epsilon:
	n += 1
	for i in range(36):												# Since the savings last 36 months, we use for loop
		monthly_return = current_savings * (r/12)					# This lets us calculate savings for 36 months
		current_savings += monthly_return + monthly_salary_savings 	
		if i % 6 == 0 :
			monthly_salary += semi_annual_raise*monthly_salary
			monthly_salary_savings = monthly_salary * guess_rate
	print(current_savings)
	if current_savings < total_down_payment: # If the 36 months saving is less than the down payment, the guessed rate is set as the new lower rate.	
		lower_rate = guess_rate

	else:
		higher_rate = guess_rate # If the 36 months saving is more than the down payment, the guessed rate is set as the new higher rate.
	
	guess_rate = (lower_rate + higher_rate)/2 						# Calculating new rate
	
	if current_savings - total_down_payment <= epsilon:	
		if guess_rate > 1:  # If the rate is too big it won't be possible to pay the downpayment after 36 months
			print('It is not possible to pay the down payment in three years')
		else:		 
			print('Best savings rate: ',guess_rate) # If the rate is below 100%, print the rate 
			print('Step in bisection search: ',n )
		break
	else:# if the difference between savings and the down payment is more than epsilon, we have to start calculating savings from start, so we need to set them to 0.
		current_savings = 0
		monthly_salary_savings = 0
		monthly_salary = annual_salary/12
		# monthly_return = current_savings * (r/12)