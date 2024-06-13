bill = float(input("How much was the bill? $"))
tip = int(input("What percentage tip would you like to give? 10 15 20:"))

num_of_people = int(input("How many people are splitting the bill? "))
tip_amount = (tip / 100) * bill
total_bill = bill + tip_amount
bill_per_person = total_bill / num_of_people
print(f"Each person should pay: ${bill_per_person:.2f}")
print(f"Tip amount: ${tip_amount:.2f}")