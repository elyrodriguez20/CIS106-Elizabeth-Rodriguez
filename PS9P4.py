def calculate_rate(code, hours):
  if code == "L":
    rate= 25.00
  else:
    if code == "A":
      rate= 30.00
    else:
      if code == "J":
        rate= 50.00
  grosspay= rate * hours
  overtime= (hours-40)* (rate*1.5)
  return grosspay

for count in range(1,6,1):
  name= input("Enter the employee's name")
  code= input("Enter the employee's code")
  hours= float(input("Enter the number of hours worked"))
  grosspay= calculate_rate(code, hours)
  print(name + " " + "gross pay is" + " " + str(grosspay))
print("The total number of employees", count)
  
  