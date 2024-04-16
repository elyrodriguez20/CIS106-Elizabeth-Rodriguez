#Connect to the file
f= open("PS8P4.txt" , "r")
item= f.readline(). rstrip('\n')
total=0
count=0
#loop as long as the last readline is not null
while item !="":
  quantity= int(f.readline())
  price= float(f.readline())
  extendedprice= quantity*price
  total= total+extendedprice
  print(item, "has a quantity of", quantity, "and a price of", price)
  item= f.readline(). rstrip('\n')
  #Increment the count
  count= count+1