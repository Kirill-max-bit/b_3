combinations = [(a, b, c) for a in [True, False] for b in [True, False] for c in [True, False]]

expressions = [
    "not (A or not B and C)",     
    "A and not (B or not C)",     
    "not (not A or B and C)"     
]


for A, B, C in combinations:
    print(f"A={A}, B={B}, C={C}")
    
    for expression in expressions:
        result = eval(expression)
        print(f"{expression} -> {result}")
        
    print()
