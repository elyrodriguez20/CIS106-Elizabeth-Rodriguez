def calculate_total(quantiy, price):
  total = quantiy * price
  if total>10000:
    total= total- (total*0.1)
  return total
    
eprice=0
loop= input("Do you want to run this program? Enter Yes or No")
while loop== "Yes":
  quantity= int(input("Enter quantity"))
  price= float(input("Enter price"))
  #call the function
  total= calculate_total(quantity, price)
  #print value returned from function
  print("Quantity purchased" , quantity, "Price per unit $", "{:.2f}".format(price), "Total is $", "{:.2f}".format(total))
  eprice= eprice+ total
  loop= input("Do you want to run this program? Enter Yes or No")
print("Totla expenses $", "{:.2f}".format(eprice))
  