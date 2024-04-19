def calculate_tuition(code, credits):
  if code == "I":
    tuition= 250.00
  else:
    if code == "O":
      tuition= 550.00
  tuition= tuition * credits
  return tuition

for count in range (1,5,1):
  name= input("Enter the student's name")
  code= input("Enter the student's code")
  credits= float(input("Enter the number of credits taken"))
  tuition= calculate_tuition(code, credits)
  print(name + " " + "tuition is" + " " + str(tuition))
print("The total number of students", count)