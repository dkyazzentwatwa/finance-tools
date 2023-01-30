def home_equity_loan(home_value, loan_amount, interest_rate, years):
    """
    This function calculates the monthly payment on a home equity loan, given a home value, loan amount, interest rate, and number of years.
    
    Parameters:
    home_value (float): the current market value of the home
    loan_amount (float): the amount borrowed for the loan
    interest_rate (float): the annual interest rate as a decimal (e.g. 0.05 for 5%)
    years (int): the number of years the loan will be paid off over
    
    Returns:
    float: the monthly payment on the loan
    """
    loan_to_value = loan_amount / home_value
    loan_interest_rate = interest_rate / 12
    loan_months = years * 12
    loan_payment = (loan_amount * loan_interest_rate) / (1 - (1 / (1 + loan_interest_rate) ** loan_months))
    return loan_payment

home_value = float(input("Enter the current market value of your home: $"))
loan_amount = float(input("Enter the amount you would like to borrow for a home equity loan: $"))
interest_rate = float(input("Enter the annual interest rate (as a decimal): "))
years = int(input("Enter the number of years you will take to pay off the loan: "))

monthly_payment = home_equity_loan(home_value, loan_amount, interest_rate, years)

print(f"Your monthly payment on the home equity loan will be ${monthly_payment:.2f}.")
