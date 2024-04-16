#connect to the file
f=open ("harperstudents.txt", "r")
name= f.readline().rstrip('\n')
totaltuition=0
count=0
#loop as long as the last readline is not null
while name !="":
  dcode= str(f.readline().rstrip('\n'))
#costrpercredit=250 if dcode== "I" else 500
  if dcode=="I":
    costpercredit=250
  else:
    costpercredit=500
  credits=int(f.readline())
  tuition= credits*costpercredit
  print(name, "Credits taken", credits, "Tuition", tuition)
  count=count+1
  totaltuition= totaltuition +tuition
  name= f.readline().rstrip('\n')
print("Total tuition", totaltuition, "number of students", count)
    