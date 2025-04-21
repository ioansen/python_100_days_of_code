import random
import my_module

print(random.randint(10,100))

print(my_module.my_number)

print(random.random())

friends = ["Alice", "Bob", "Cosmin", "Yalamina", "Emanuel Bonaparte"]

print(friends[random.randint(0,4)])
print(random.choice(friends))