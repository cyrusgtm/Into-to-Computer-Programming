# Initial annual salary of a person.
initial_annual_salary = float(input('Enter your starting annual salary: '))


# Initial value of different variables.
cost = 1000000
portion_down_payment = 0.25 
down_payment = cost * portion_down_payment
semi_annual_raise = .07
annual_return = 0.04
epsilon = 100


# Initializing variables for bisection method.
# Highest possible rate.
higher_rate = 10000
# lowest possible rate.
lower_rate = 0
# Initially I set our main rate as the highest rate. 
guess_rate = (higher_rate+lower_rate)/2



# Initialize the bisection method steps.
steps = 0
# Setting our initial condition for our while statement. We will check later in the
# program if it is possible to pay the payment in three years or not. Therefore, 
# initially, we are assuming it is possible.
possible_in_three_years = True


# Main program
while True:
    steps += 1
    annual_salary = initial_annual_salary
    # Since our rate is usually between 0 to 100%, and we are printing our rate in
    # decimals we have to divide our rate by 10000. It is because even if our optimum
    # rate is 10000, our rate will still be 1.
    main_rate = guess_rate / 10000
    monthly_savings = (annual_salary/12) * main_rate
    
    # Our initial savings and initial months.
    current_savings = 0.0
    months = 0
    print("guess=", guess_rate) #checker 
    # Since we are calculating the savings for 36 months, we use for loop to iterate
    # if for 36 times.
    for months in range(1,37):        
        current_savings += monthly_savings + (current_savings * (annual_return / 12))
        # Increasing the salary after every 6 months.    
        if months % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise
            monthly_savings = (annual_salary/12)* main_rate
    print("i= ",  months, "savings= ", current_savings) #checker          
    

    # Now we need to check if our current_savings is more than or less than our
    # down payment. After 36 months if our savings is more than down_payment
    # we set our higher rate to be guess rate(setting our upper limit) and vice versa 
    # if the savings is less than guess rate.
    if current_savings > down_payment:
        higher_rate = guess_rate
    else:
        lower_rate = guess_rate
    

    # While searching for our main_rate if our lower rate is greater than or equal to
    # higher rate, then we declare that it is not possible to pay the down payment. This is
    # because our higher rate is 1 which is 100% of our salary and we can't pay more than our
    # salary.
    if lower_rate >= higher_rate:
        possible_in_three_years = False
        break
        
    guess_rate = (higher_rate + lower_rate) // 2     # Using floor division(//) for less numbers after decimal

    # Now we have to check the difference between our current savings and down payment. 
    # If the difference is smaller or equal to epsilon then we don't need any more iteration.
    if abs(current_savings - down_payment) <= epsilon:
        break
    
# If we can pay the payment in three years we can print the rate and no of steps.
# If we can't we print that it is not possible.
if possible_in_three_years:
    print('Best savings rate:',main_rate)
    print('Steps in bisection search:',steps)
else:
    print('It is not possible to pay the down payment in three years.')

