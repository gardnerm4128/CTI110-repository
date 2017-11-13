# CTI-110
# M2HW2 - Tip Tax Total
# Matthew Gardner
# 09/13/2017

#ask food price
price = float(input("price of food? (in usd)"))
#ask tip
#tip = float(input("total tip? (in usd)"))
#ask sales tax
#salesTax= float(input("sales tax? (in dec)"))
#calc tip
tip = .18 * price
print("tip amount is", tip, "usd.")
#calc sales tax
salesTax = .07 * price
print("sales tax is", salesTax, "usd.")
#calc total cost
totalCost = price + tip + salesTax
print("total Cost is", totalCost, "usd.")


