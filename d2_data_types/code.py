len("12345")

print(type("1223"))
print(type(12345))
print(type(123.45))
print(type(True))
print(type([1,2,3]))
print(type((1,2,3)))
print(type({1,2,3}))
print(type(range(1,6)))
print(type(list(range(1,6))))

print(range(6))
print(list(range(6)))

print(6/2)
print(6//2)
print(7//2)

#PEMDAS
# ()
# unary + - not ~
# **
# * /
# + -
# << >>
# &
# | ^
# <=, <, >=, >
# and
# or


print( 1 & 0 )
print( 1 | 0 )
print( 1 ^ 0 )
print( 1 << 1)
print( 1 >> 3)
print ( 1 << 1 + 1 >> 3)
print( 5 <= 2 << 2 >= 4)
print( 5 <= 8 >= 4)
print (2 & 2)
print( 5 <= 8 & 7 >= 4)
print( 5 <= 8 and 7 >= 4)
print (4 < 7 & 8)

score = 0
height = 1.8
is_winning = True

print(f'Your score is = {score}, your height is = {height}. Your are wining: {is_winning}')