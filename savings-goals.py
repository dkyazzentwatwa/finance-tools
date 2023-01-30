#####################
# SAVINGS GOALS CALCULATOR #
# By David Kyazze-Ntwatwa #
#####################

def savings_goal(goal, monthly_savings, interest_rate):
    """
    This function calculates the number of months required to save a certain amount, given a fixed monthly savings amount and interest rate.
    
    Parameters:
    goal (float): the savings goal amount
    monthly_savings (float): the fixed monthly savings amount
    interest_rate (float): the annual interest rate as a decimal (e.g. 0.05 for 5%)
    
    Returns:
    int: the number of months required to save the goal amount
    """
    balance = 0
    monthly_interest_rate = interest_rate / 12
    months = 0
    while balance < goal:
        months += 1
        balance += monthly_savings
        interest = balance * monthly_interest_rate
        balance += interest
    return months

goal = float(input("Enter your savings goal: $"))
monthly_savings = float(input("Enter the monthly savings amount: $"))
interest_rate = float(input("Enter the annual interest rate (as a decimal): "))

months_to_reach_goal = savings_goal(goal, monthly_savings, interest_rate)

print(f"It will take you {months_to_reach_goal} months to reach your savings goal.")
