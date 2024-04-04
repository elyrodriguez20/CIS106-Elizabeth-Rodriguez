print("Enter the quantity of widgets")
amount = float(input())
quantity= amount 
print("Enter the price per widgets")
price = float(input())
if quantity>10000:
  price= 10.00
else:
  if quantity> 5000:
    price= 20.00
  else:
    if quantity<50000:
      price= 30.00
extprice= quantity * price
tax= extprice * 0.07
total= extprice + tax
print("The extended price is $" , " {: .2f}".format(extprice))
print("The tax is $" , " {: .2f}".format(tax))
print("The total is $", " {: .2f}".format(total))
