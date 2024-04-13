control= str(input("Enter Yes if you would like to run this program"))
totalpay= 0
numberemp=0
while control == "Yes":
  name= str(input("Enter the Employee's name"))
  hours= float(input(" Enter the number of hours worked"))
  payrate= float(input("Enter the employee's hourly pay"))
  if hours <=40:
    pay=hours *payrate
  else:
    pay=40*payrate + (hours-40)*1.5 *payrate
    print("The weekly pay for", name, "is $",pay)
  totalpay= totalpay+pay
  numberemp=numberemp+1
  control= str(input("Enter Yes if you would like to run this program"))
print("The total gross pay is $", totalpay)
averagepay=totalpay/numberemp
print("The average pay is $", averagepay)
  