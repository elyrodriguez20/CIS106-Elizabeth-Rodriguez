from PS10P1 import sales_forecast

control= str(input("Enter Yes if you would like to run this program "))
while control.lower()== "yes":
  name= input("Enter the salesperson's name")
  month= input("Enter the month in 3 letter e.g. Feb")
  month=month.lower()
  sales= float(input("Enter the sales made"))
  forecasted_sales= sales_forecast(month,sales)
  print("Salesperson", name, " Will sell","{:.2F}".format(forecasted_sales))
  control= str(input("Enter Yes if you would like to run this program"))

from PS10P1 import saquare_footage

control= str( input("Enter Yes if you would like to run this program "))
while control.lower()== "yes":
  length= float( input("Enter the length of the room"))
  width= float( input("Enter the width of the room"))
  height= float( input("Enter the height of the room"))
  sf= saquare_footage(length, width, height)
  paint= sf/50
  print("The square footage of the room is", sf, "is", " {:.2F}".format(sf))
  control= str(input("Enter Yes if you would like to run this program "))


from PS10P1 import discount_prices

control= str( input("Enter Yes if you would like to run this program "))
while control.lower()== "yes":
  quantity= int( input("Enter the quantity of the item"))
  price= float( input("Enter the price of the item"))
  discount= float( input("Enter the discount percentage"))
  discprice= discount_prices(price, discount)
  discprice= (quantity*price) * discount
  total= (quantity*price)- discprice
  print("The total discounted price of the item is", " {:.2F}".format(total))
  print("The total discount amount of the item is", " {:.2F}".format(discprice))
  control= str(input("Enter Yes if you would like to run this program "))