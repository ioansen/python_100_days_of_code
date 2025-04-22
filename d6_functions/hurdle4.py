def turn_right():
    for i in range(3):
        turn_left()


def mov(n):
    for i in range(n):
        move()


def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


def hurdle():
    move()
    jump()


def jumplong():
    steps = 0
    while wall_in_front():
        turn_left()
        move()
        turn_right()
        steps += 1

    move()
    turn_right()

    for i in range(steps):
        move()

    turn_left()


while not at_goal():
    if wall_in_front():
        jumplong()
    else:
        move()