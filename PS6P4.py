print("Enter number of concert tickets")
tickets= int(input())
print("Enter price per ticket")
price= float(input())

if tickets > 25:
  price= 50.00
else:
  if tickets > 10 and 24:
    price= 60.00
  else:
    if tickets > 5 and 9:
      price= 70.00
    else:
      price= 75.00
total= tickets * price 
print("The number of tickets is" + " " + str(tickets))
print("The price per ticket is" + " " + str(price))
print("The total cost is" + " " + str(total))