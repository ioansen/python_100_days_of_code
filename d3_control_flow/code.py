print("welcome to the rollercoaster!")

height = int(input("input your height sir: \n"))

if height >= 120:
    print("you sir can roll today")
    age = int(input("sir, what is your age sir?"))
    bill = 0
    if age <= 12:
        print("price is 50")
        bill = 50
    elif age <= 18:
        print("price is 157 sir, please pay now")
        bill = 157
    else:
        print("please sir, the price is 2 thousand hundred dollars")
        bill = 200_000

    wants_photo = input("do you want to be stocked sir? Blink once for yes, twice for no")
    if wants_photo == "y":
        bill += 3

    print (f'your final bill is {bill} us american dollars')
else:
    print("sorry sir, you cannot ride the rollercoaster today, not today")


r = height

print(f'{r} is even') if r % 2 == 0 else print(f'{r} is odd')

print("yo")

print('''
               __/\\__
              `==/\\==`
    ____________/__\\____________
   /____________________________\
     __||__||__/.--.\\__||__||__
    /__|___|___( >< )___|___|__\
              _/`--`\\_
             (/------\\)
''')