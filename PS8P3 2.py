#Connect to the file
f= open("PS8P3.txt" , "r")
name= f.readline()
salary=0
bonusrate=0
bonus=0
totalbonus=0
count=0
#loop as long as the last readline is not null
while name !="":
  salary= float(f.readline())
  if salary>= 100000:
    bonus= salary*0.20
  else:
    if salary>=50000:
      bonus= salary*0.15
    else:
      bonus= salary*0.10
#salary= f.readline().rstrip('\n')  #bonusrate=float(f.readline())
#bonus=float(salary)*float(bonusrate)
  totalbonus= totalbonus+bonus
  print(name, "has a salary of", salary, "and a bonus of", bonus)
  name= f.readline().rstrip('\n')
