# Условия для проверки
x = 5
y = 6

# а) х > 2 и у > 3
condition_a = x > 2 and y > 3

# б) х > 1 или y <= 2
condition_b = x > 1 or y <= 2

# в) х >= 0 и у < 5
condition_c = x >= 0 and y < 5

# г) х > 3 или x <= 1
condition_d = x > 3 or x <= 1

# д) х > 3 и x < 10
condition_e = x > 3 and x < 10

# е) неверно, что х > 2
condition_f = not (x > 2)

# ж) неверно, что х > 0 и х < 5
condition_g = not (x > 0 and x < 5)

# з) 10 < x <= 20
condition_h = 10 < x <= 20

# и) 0 < y <= 4 и x < 5
condition_i = 0 < y <= 4 and x < 5

# Вывод результатов
print("а) х > 2 и у > 3:", condition_a)
print("б) х > 1 или y <= 2:", condition_b)
print("в) х >= 0 и у < 5:", condition_c)
print("г) х > 3 или x <= 1:", condition_d)
print("д) х > 3 и x < 10:", condition_e)
print("е) неверно, что х > 2:", condition_f)
print("ж) неверно, что х > 0 и х < 5:", condition_g)
print("з) 10 < x <= 20:", condition_h)
print("и) 0 < y <= 4 и x < 5:", condition_i)
