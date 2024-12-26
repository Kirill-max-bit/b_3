# Возможные комбинации значений X и Y
combinations = [(True, True), (True, False), (False, True), (False, False)]

# Функция для вычисления каждого выражения
def compute_expressions(X, Y):
    a = not (X or Y)
    b = not X and Y
    c = X and not Y
    
    return a, b, c

# Перебор всех комбинаций и вывод результатов
for X, Y in combinations:
    a, b, c = compute_expressions(X, Y)
    print(f"X={X}, Y={Y}:")
    print(f"\ta) не (X или Y) = {a}")
    print(f"\тб) не X и Y = {b}")
    print(f"\tв) X и не Y = {c}")
    print()
    