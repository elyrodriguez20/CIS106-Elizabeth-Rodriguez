print("Enter the name of the appliance")
appliance= input()
print("Enter the cost of the appliance")
cost= float(input())
if cost> 1000.00:
  warranty= cost* 0.10
else: 
  warranty = cost * 0.05

print("The name of appliance is", appliance)
print("The cost of the warranty is", warranty)
print("The total cost is", cost+ warranty)


  