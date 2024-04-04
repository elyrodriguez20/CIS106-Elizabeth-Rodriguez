print("Enter the user's name")
name= input()
print("Enter the number of dependents")
dependents= int(input())
print("Enter the gross income")
grossincome= float(input())
adjustedgrossincome= grossincome- dependents*12000
if adjustedgrossincome> 50000.00:
  taxrate= 0.20
else:
  taxrate= 0.10
  incometaxrate= adjustedgrossincome * taxrate
  if incometaxrate< 0.00:
    incometaxrate= 100.00
    print("The name of the user is", name)
    print("The gross income is", grossincome)
    print("The number of dependents is", dependents)
    print("The adjusted gross income is", adjustedgrossincome)
    print("The income tax is", incometaxrate)
    
