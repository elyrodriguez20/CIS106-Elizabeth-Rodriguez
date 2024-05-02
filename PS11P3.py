def display(names,exam):
  for i in range(1,6,1):
    print(names[i], exam[i])
def reverse(names,exam):
  for i in range(len(names)-1,-1,-1):
    print(names[i], exam[i])

def highest(names,exam):
  highest= exam[0]
  for i in range(1,6,1):
    if exam[i]>highest:
      highest= exam[i]
  print(highest)
    

names= ['Luis', 'Jon', 'Ana', 'Jose', 'Ely', 'Caro']
exam=[85,60,65,90,100,95]

#Call the function
display(names,exam)
reverse(names, exam)
highest(names, exam)
