# Возможные комбинации значений А и В
num = [(True, True), (True, False), (False, True), (False, False)]

# Функция для вычисления каждого выражения
def compute_expressions(A, B):
    a = not (A and B)
    b = not A or B
    c = A or not B
    
    return a, b, c

# Перебор всех комбинаций и вывод результатов
for A, B in num:
    a, b, c = compute_expressions(A, B)
    print(f"А={A}, B={B}:")
    print(f"\ta) не (А и В) = {a}")
    print(f"\тб) не А или В = {b}")
    print(f"\tв) А или не В = {c}")
    print()
