def calculate_destination_city(miles, gallons):
  mpg= miles/gallons
  return mpg

count=0
loop= input("Do you want to run this program? Enter Yes or No")
while loop== "Yes":
  destcity= str(input("Enter the distintation"))
  miles= int(input("Enter the number of miles driven"))
  gallons= int(input("Enter the number of gallons used"))
  mpg= calculate_destination_city(miles, gallons)
  print("The destination city is", destcity, "The miles are", miles,  "Miles per gallon is", mpg)
  count= count+1
  loop= input("Do you want to run this program? Enter Yes or No")
print("Total number of trips", count)