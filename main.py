paid = 1000 * 32.87
sold = 1000 * 33.92
profit = (sold - sold * 0.02)-(paid + paid * 0.02)

if profit > 0:
    print("Joe madde a profit of", round(profit, 2))
else:
    print("Joe lost $", round(abs(profit),2))
