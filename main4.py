print("Enter the first name")
first_name= input()
print("Enter the number of steps walked in a day")
steps_walked= int(input())
print("Enter how many calories you burned per step")
calories_per_step= float (input())
calories_burned= steps_walked * calories_per_step
print(first_name, "you burned", calories_burned)
#Amount of calories burned is calculated by multiplying the number of steps walked by the calories burned per step
