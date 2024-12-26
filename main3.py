A = True
B = False
C = False

# а) не А и B
result_a = not A and B
print(f"а) {result_a}")

# б) А или не B
result_b = A or not B
print(f"б) {result_b}")

# в) А и B или C
result_c = (A and B) or C
print(f"в) {result_c}")
