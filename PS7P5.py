control= str(input("Enter Yes if you would like to run this program"))
discountprice=0
extprice= 0
discount= 0
while control== "Yes":
  quantity= int(input("Enter the quantity of the item"))
  price= float(input("Enter the price of the item"))
  extprice= quantity*price
  if extprice >= 10000:
    discount= 0.25
  else: 
    discount= 0.10
  discountprice= extprice - extprice*discount
  print("The extended price is $", extprice)
  print("The discountamount is $", extprice*discount)
  print("The total is $", extprice- discount)
  control= str(input("Enter Yes if you would like to run this program"))
  totaldiscount= totaldiscount+ discount
print("The total discount is $", totaldiscount)
print("This is the sum of the discounts", totaldiscount)
         