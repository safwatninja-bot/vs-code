actual_cost = float(input("please enter the actual amount of price:"))
sale_amount = float(input("please enter the sells amount of price:"))

if (sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    print("total profit = {0}".format(amount))
else:
    print("no profit!!")