def calculate_profit(amount_invested, stock_price, shares, stop_loss, take_profit):
    purchase_price = stock_price * shares
    if amount_invested < purchase_price:
        return "Error: Not enough investment for shares."
    stop_loss_amount = (stock_price - stop_loss) * shares
    take_profit_amount = (take_profit - stock_price) * shares
    if stop_loss_amount > 0:
        expected_profit = -stop_loss_amount
    elif take_profit_amount > 0:
        expected_profit = take_profit_amount
    else:
        expected_profit = 0
    return expected_profit

amount_invested = float(input("Enter amount invested: "))
stock_price = float(input("Enter stock price: "))
shares = int(input("Enter number of shares: "))
stop_loss = float(input("Enter stop-loss price: "))
take_profit = float(input("Enter take-profit price: "))

expected_profit = calculate_profit(amount_invested, stock_price, shares, stop_loss, take_profit)
print(f"Expected Profit: ${expected_profit:.2f}")