print("welcome son")
total_bill = int(input("What was the total bill son?\n"))
tip_pct = int(input("How much percentage tip would you like to give?\n"))
number_of_ppl = int(input("And lastly, my friend, how many people are there that are generous enough to split this outrageous bill?\n"))

total_bill *= 1 + tip_pct/100

print(f'Each person should give oh {round(total_bill/number_of_ppl, 2)}')