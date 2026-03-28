import math


principal = 0
interest = 0
time = 0
while principal <= 0:
  principal = float(input("What is your prinicipal?: "))
  if principal <= 0:
    print("Please enter a valid number")
while interest <= 0:
  interest = float(input("What is your interest?: "))
  if interest <=0:
    print("Please enter a valid number")
while time <= 0:
   time = float(input("How long is the bond?: "))
   if interest <=0:
     print("Please enter a valid number")
final_amount = round(principal*pow((1+interest/100), time), 2)
print(f"The final amount will be ${final_amount: ,}.")
