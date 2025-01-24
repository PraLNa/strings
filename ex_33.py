n = int(input("Введите натуральное число: "))

even_numbers = []

for i in range(1, n + 1):
    if i % 2 == 0:
        even_numbers.append(i)

print("Четные числа от 1 до", n, ":", " ".join(map(str, even_numbers)))
