print("Enter a principle amount of a CD")
principle = float(input())
print("Enter the year to maturity of the CD")
year = int(input())
if principle > 100000 and year ==5:
  interest= 0.06
else:
  if principle > 50000 and year == 10:
    interest= 0.05
  else:
    if principle >50000 and year ==5:
      interest= 0.04
    else:
      interest= 0.02
firstyeartotal= principle * interest 
print("Principle: " + str(principle))
print("Interest: " + str(interest))
print("First year total: " + str(firstyeartotal))
