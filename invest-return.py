#####################
# INVESTMENT RETURN CALCULATOR #
# By David Kyazze-Ntwatwa
#####################

def investment_return(principal, rate, years):
    """
    This function calculates the future value of an investment, given a principal amount, interest rate, and number of years.
    
    Parameters:
    principal (float): the initial investment amount
    rate (float): the annual interest rate as a decimal (e.g. 0.05 for 5%)
    years (int): the number of years the investment will grow
    
    Returns:
    float: the future value of the investment
    """
    return principal * (1 + rate) ** years

principal = float(input("Enter the initial investment amount: $"))
rate = float(input("Enter the annual interest rate (as a decimal): "))
years = int(input("Enter the number of years the investment will grow: "))

future_value = investment_return(principal, rate, years)

print(f"The future value of your investment will be ${future_value:.2f}.")
