def calculate_batting_average(hits, at_bats):
  batting_average= hits/at_bats
  return batting_average

for count in range (1,10,1):
  name= input("Enter the player's name")
  hits= int(input("Enter the number of hits"))
  at_bats= int(input("Enter the number of at bats"))
  batting_average= calculate_batting_average(hits, at_bats)
  print(name + " " + "batting average is" + " " + str(batting_average))
print("Total number of players", count)
