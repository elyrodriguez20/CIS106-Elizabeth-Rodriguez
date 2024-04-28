def calculate_total(quantity,price):
  global total 
  global tax 
  total= quantity*price
  tax=total*.07
  total+=tax
  return()

loop= input("Do you want to run this program? Enter Yes or No ")
while loop == "Yes":
  quantity= int(input("Enter the quantity"))
  price= float(input("Enter the price"))

  #call the function
  calculate_total(quantity,price)
  #print value returned from function
  print("The total is $"," {:.2F}".format(total), "The tax amount $ "," {:.2F}".format(tax))
  loop= input("Do you want to run this program? Enter Yes or No ")