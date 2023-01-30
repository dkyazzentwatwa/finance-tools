#####################
# RETIREMENT SAVINGS  CALCULATOR #
# By David Kyazze-Ntwatwa #
#####################


def retirement_savings(current_age, retirement_age, monthly_savings, interest_rate):
    """
    This function calculates the amount saved for retirement, given a current age, retirement age, monthly savings amount, and interest rate.
    
    Parameters:
    current_age (int): the current age of the individual
    retirement_age (int): the age at which the individual plans to retire
    monthly_savings (float): the fixed monthly savings amount
    interest_rate (float): the annual interest rate as a decimal (e.g. 0.05 for 5%)
    
    Returns:
    float: the amount saved for retirement
    """
    months = (retirement_age - current_age) * 12
    balance = 0
    monthly_interest_rate = interest_rate / 12
    for _ in range(months):
        balance += monthly_savings
        interest = balance * monthly_interest_rate
        balance += interest
    return balance

current_age = int(input("Enter your current age: "))
retirement_age = int(input("Enter your retirement age: "))
monthly_savings = float(input("Enter the monthly savings amount: $"))
interest_rate = float(input("Enter the annual interest rate (as a decimal): "))

retirement_savings = retirement_savings(current_age, retirement_age, monthly_savings, interest_rate)

print(f"You will have ${retirement_savings:.2f} saved for retirement.")
