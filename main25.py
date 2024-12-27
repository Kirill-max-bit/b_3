from itertools import product

combinations = list(product([True, False], repeat=3))


expressions = [
    "(not (A and B)) and (not A or not C)", 
    "not (A and not B) or (A or not C)",    
    "A and not B or not (A or not C)"        
]

print("Комбинация\t| Результат")
print("-" * 50)

for A, B, C in combinations:
    print(f"{A=}\t{B=}\t{C=}", end="\t|\t")

    for expression in expressions:
        result = eval(expression)
        print(result, end="\t")

    print()
