def cash_flow(monthly_income, monthly_expenses):
    """
    This function calculates the monthly cash flow, given the monthly income and expenses.
    
    Parameters:
    monthly_income (float): the monthly income amount
    monthly_expenses (float): the monthly expenses amount
    
    Returns:
    float: the monthly cash flow amount
    """
    return monthly_income - monthly_expenses

monthly_income = float(input("Enter your monthly income: $"))
monthly_expenses = float(input("Enter your monthly expenses: $"))

monthly_cash_flow = cash_flow(monthly_income, monthly_expenses)

if monthly_cash_flow >= 0:
    print(f"Your monthly cash flow is ${monthly_cash_flow:.2f}, which is positive.")
else:
    print(f"Your monthly cash flow is ${monthly_cash_flow:.2f}, which is negative.")
