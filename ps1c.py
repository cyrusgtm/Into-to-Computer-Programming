# Salary of the person
annual_salary = float(input('Enter your annual salary: '))


# Semi annual raise
semi_annual_raise = 0.07
# Cost of the house
cost = 1000000


# Different monthly salary saving rates. This is initialized for the bisection search
# algorithm. Our goal is to search for a rate that  is between these two rates to find the most
# optimal rate.
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



# Important initial values
current_savings = 0
# Interest rate of investment.
r = 0.04
# Initial steps in bisection
n = 0 


# Main program. This program runs until its not terminated by using
# false.
while True:
	# Since the savings lasts 36 months, we use for loop to calculate the savings from 
	# 1 to 37 which iterates 36 times.
	n += 1
	for i in range(1, 37):												
		monthly_return = current_savings * (r/12)					
		current_savings += monthly_return + monthly_salary_savings
		# There is semi-annual increase in salary, so this part checks if the no of 
		# months is 6 or a multiple of 6 and increases the salary. 	
		if i % 6 == 0 :
			monthly_salary += semi_annual_raise*monthly_salary
			monthly_salary_savings = monthly_salary * guess_rate

	# After saving for 36 months, this part checks if our saving is higher or lower than 
	# our total down_payment. If the total down payment is higher than the savings than 
	# our lower rate is set as the rate we used to calculate the savings. However, if the 
	# total down payment is lower than the current savings then the higher rate is set as 
	# our guessed rate above.
	if current_savings < total_down_payment: 
		lower_rate = guess_rate
	else:
		higher_rate = guess_rate 
	# Using the changed rate from the above part of our code, we calculate our new guess rate
	# which will be used to calculate our savings.
	guess_rate = (lower_rate + higher_rate)/2 						
	

	# We didn't check if the difference of savings and the down payment is below epsilon
	# or not. Therefore in this code, we calculate difference and if the difference is below epsilon
	# we do not need to run our program more/stop the iteration. If the difference is more we need to initialize our value
	# of current_savings, monthly_salary_savings and monthly_salary so that we don't have any value saved
	# before we start iteration the for loop above.
	if current_savings - total_down_payment <= epsilon:			# If the difference is small or equal
	# Sometimes, even if the difference is small we can't save enough in 36 months to pay our down 
	# payment. To check if we can't save enough money, we have to disregard the our process if
	# the guess_rate is 1. This is because, for eg: when the guess rate is 0.44, we have to save 44% of our salary
	# for the down payment. However, if the guess rate is more than 1 that means we have to save more than
	# 100% of our saving which is not possible, cause you only have you 100% of your salary to put in the
	# savings.
		if guess_rate > 1:
			print('It is not possible to pay the down payment in three years')
		else:
			False		 
			print('Best savings rate is {}'.format(guess_rate)) 
			print('Step in bisection search: {} '.format(n) )
		break
	else:														# If the difference is big initialize parameters.
		current_savings = 0
		monthly_salary_savings = 0
		monthly_salary = annual_salary/12
		# monthly_return = current_savings * (r/12)
