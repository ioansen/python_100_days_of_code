import random
import string

# ask user for how many of each
num_letters = int(input("How many letters? "))
num_symbols = int(input("How many symbols? "))
num_numbers = int(input("How many numbers? "))

# generate lists of random chars
letters = [random.choice(string.ascii_letters) for _ in range(num_letters)]
symbols = [random.choice(string.punctuation)    for _ in range(num_symbols)]
numbers = [random.choice(string.digits)         for _ in range(num_numbers)]

# combine all characters
password_chars = letters + symbols + numbers

# shuffle in-place to randomize positions
random.shuffle(password_chars)

# join into final password string
password = ''.join(password_chars)

print("Your password is:", password)
