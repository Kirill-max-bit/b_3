combinations = [
    (True, True, True),
    (True, True, False),
    (True, False, True),
    (True, False, False),
    (False, True, True),
    (False, True, False),
    (False, False, True),
    (False, False, False)
]


expressions = [
    "(not (X or Y)) and (not X or not Z)",  
    "not (not X and Y) or (X and not Z)",   
    "X or not Y and not (X or not Z)"       
]


for X, Y, Z in combinations:
    print(f"X={X}, Y={Y}, Z={Z}")

    for expression in expressions:
        result = eval(expression)
        print(f"{expression} -> {result}")

    print()
