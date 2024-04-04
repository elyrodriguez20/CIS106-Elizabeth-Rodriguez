print("Enter a quantity of an item")
qty= float(input())
if qty>= 1000:
  unitprice=3.00
else:
  unitprice= 5.00
  print("compute the extended price")
  extprice= qty * unitprice
  tax= extprice * 0.07
  total= extprice + tax
  print("Quantity:", qty)
  print("Unit price:", unitprice)
  print("Extended price:", extprice)
  print("Tax amount:", tax)
  print("Total:" ,total)
  