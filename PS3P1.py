#this program will comput investment in stock
print("enter stock symbol you want to buy")
symbol = str(input())
print ("number of share you want to buy")
shares= float(input())
print ("enter the cost per share")
cost = float(input())
investment= shares *cost 
print("The investment in " + symbol + " "+  "is" + " "+ str(investment))
