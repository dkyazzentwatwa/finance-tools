#####################
# CREDIT PAYMENT CALCULATOR #
# By David Kyazze-Ntwatwa
#####################

print("Calculate how long it will take to payoff your credit balance!")

balance = 0

def credit_card_payoff(balance, interest_rate, monthly_payment):
    """
    This function calculates the number of months required to pay off a credit card balance, given a fixed monthly payment and interest rate.
    
    Parameters:
    balance (float): the initial credit card balance
    interest_rate (float): the annual interest rate as a decimal (e.g. 0.05 for 5%)
    monthly_payment (float): the fixed monthly payment amount
    
    Returns:
    int: the number of months required to pay off the credit card balance
    """
    monthly_interest_rate = interest_rate / 12
    months = 0
    while balance > 0:
        months += 1
        interest = balance * monthly_interest_rate
        balance += interest
        balance -= monthly_payment
    return months

balance = float(input("Enter the credit card balance: $"))
interest_rate = float(input("Enter the annual interest rate (as a decimal): "))
monthly_payment = float(input("Enter the monthly payment: $"))

#calculates how many months left to pay.
months_to_payoff = credit_card_payoff(balance, interest_rate, monthly_payment)

print("It will take you", months_to_payoff, "months (",(months_to_payoff / 12),"years )to pay off your credit card.")
