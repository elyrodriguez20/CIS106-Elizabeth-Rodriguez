print( "enter how much you paid for your meal") #Asking user how much they padi for their meal
meal= float(input())
tip15= meal * .15 #computing tip at 15%
tip18= meal * .18 #computing tip at 18%
tip20= meal * .20 #compting tip at 20%
meal_str= "{:.2f}" .format(meal)
#printing with 15% tip
print("With 15% Tip:", "\n Total:","$","{:.2F}".format(meal),"\n Tip:", "{:.2F}".format(tip15),"\n Total with tip: "," {:.2F}".format(meal + tip15))
#print with 18% tip
print("With 18% Tip:", "\n Total:", "{:.2F}".format(meal),"\n Tip:", "{:.2F}".format(tip18), "\n Total with tip:"," {:.2F}".format(meal + tip18))
#print with 20% Tip
print("With 20% Tip:", "\n Total:  "," {:.2F}".format(meal), "\n Tip: "," {:.2F}".format(tip20), "\n Total with tip:"," {:.2F}".format(meal +tip20))

