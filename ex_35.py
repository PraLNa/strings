A = int(input("Введите A: "))
B = int(input("Введите B: "))
K = int(input("Введите K: "))

numbers = list(range(A, B + 1, K))

print("Числа от A до B с шагом K:", ' '.join(map(str, numbers)))
