# main.py

shares = 1000
buy, sell = 32.87, 33.92
buy_comm, sell_comm = 0.02, 0.02

buy_total = shares * buy
sell_total = shares * sell
net = sell_total*(1-sell_comm) - buy_total*(1+buy_comm)

print("Paid: $", round(buy_total,2))
print("Buy commission: $", round(buy_total*buy_comm,2))
print("Received: $", round(sell_total,2))
print("Sell commission: $", round(sell_total*sell_comm,2))
print("Net money: $", round(net,2), "→", "Profit" if net>0 else "Loss")
