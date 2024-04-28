def student_scores(name, e1, e2, e3):
  total= e1+e2+e3
  average= total/3
  return name, total, average

control= str( input("Enter Yes if you would like to run this program "))
while control.lower()== "yes":
  name= str( input("Enter the student's name"))
  e1= float( input("Enter the first exam score"))
  e2= float( input("Enter the second exam score"))
  e3= float( input("Enter the third exam score"))
  name, total, average= student_scores(name, e1, e2, e3)
  print("The total score for", name, "is", total)
  print("The average score for", name, "is", average)
  control= str( input("Enter Yes if you would like to run this program "))
  