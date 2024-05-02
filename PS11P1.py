def display(names):
  for i in names:
    print(i)
def reverse(names):
  for i in range(len(names)-1,-1,-1):
    print(names[i])


names= ['Luis', 'Jon', 'Ana', 'Jose', 'Ely', 'Caro']

#call the function
display(names)
reverse(names)