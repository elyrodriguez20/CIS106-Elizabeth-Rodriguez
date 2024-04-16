print("make of the car")
make= str(input())
print(" model of the car")
model= str(input())
print("msrp for the car")
mrsp= float(input())
print("discount percent for car")
discount= float(input())
amount= mrsp * discount
print(make + " " + "is make of the car" + " "+  model + " " +" is model of the car")
print( str(mrsp) + " "+ "is the mrsp of the car")
print(str(discount) + " " + "is the discount percent of the car")
print(str(amount) + " is the amount off the car")
discountedprice= mrsp-amount
print(str(discountedprice) + " is the discounted price of the car")



