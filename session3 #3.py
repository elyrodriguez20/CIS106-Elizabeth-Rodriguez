# Taking input for number of books and total cost per book
print("Enter the number of books to order")
books= int(input())
print("Enter the cost per book")
costperbook= float(input())
totalcost= books* costperbook

#check if order is free
if totalcost >50.00:
  shippingcost= 0.00
else:
  shippingcost= 25.00

  #Display order total and shipping cost 
print("The order total is", totalcost)
print("The shipping cost is", shippingcost)
  