def evaluate_expression(expression, X, Y, Z):
    return eval(expression)


num = [
    "not (Y or not X and Z) or Z",
    "X and not (not Y or Z) or Y",
    "not (X or Y and Z) or not X"
]


for X in [True, False]:
    for Y in [True, False]:
        for Z in [True, False]:
            print(f"X={X}, Y={Y}, Z={Z}")
            for expression in num:
                result = evaluate_expression(expression, X, Y, Z)
                print(f"{expression} -> {result}")
                print()
