#Connect to file
f=open("10players.txt", "r")
name= f.readline(). rstrip('\n')
players=[]
Batting=[]

def display(players,Batting):
  for i in range(1,10,1):
    print(players[i], Batting[i])

while name!= "":
  players.append(name)
  Batting.append(f.readline())
  name= f.readline(). rstrip('\n')
#Call the function
display(players,Batting)

search=input("Enter yes if you would like to search for a player")  
while search=="yes":
  found="no"
  lookfor= input("Enter the name of the player")
  for who in players:
    if who== lookfor:
      print(lookfor, "Their batting average is", Batting[players.index(who)])
      found= "yes"
  search= input("Do you want to search for another player?")
    
    


