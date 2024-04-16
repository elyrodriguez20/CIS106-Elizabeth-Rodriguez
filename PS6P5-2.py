print("Enter employees last name")
lastname= input()
print("Enter employees salary")
salary= float(input())
print("Enter employees level")
level= int(input())
if level > 10:
  bonusrate= 0.25
else:
  if level >5 and  9:
    bonusrate= 0.2
  else:
    bonusrate= 0.1
bonus= salary * bonusrate
print("Employees last name is" + " " + lastname)
print("Employees bonus is" + " " +str(bonus))
      