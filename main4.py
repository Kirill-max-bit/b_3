# Задаем исходные значения переменных
X = True
Y = True
Z = False

# а) не X и Y
print(not X and Y)

# б) X или не Y
print(X or not Y)

# в) X или Y и Z
print(X or (Y and Z))
