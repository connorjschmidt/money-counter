print("homework of 7/14: Balance")

print()

print("Create a program that calculates how much money you have for the next 3 weeks (incuding the current week) if: you start out with $43.00, you make $547.02 a week, and after the second week, you spend $100 on a drone.")

print()

balance = 43 
income = 547.02
droneCost = 100

print("Balance: ")

for i in range(1,3,1):
  balance += (i*income)
  print("Week {}: You have ${}.". format(i,balance))

for i in range(3,5,1):
  balance += (i*income-droneCost)
  print("Week {}: You have ${}.".format(i,balance))