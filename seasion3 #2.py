print("Program asked user for an item")
item=input("Enter an item:")
print("Program asked user for a quantity")
quantity= float(input())
A= 10.00
B= 20.00
if item=="A":
  unitprice=10.00
else:
  unitprice=20.00

extendedprice= quantity* unitprice

#print the item, unit price, and extended price
print("The item is", item)
print("The unit price is:" , unitprice)
print("The extended price is", extendedprice)
