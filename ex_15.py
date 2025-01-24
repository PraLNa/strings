# Дано положительное действительное число. Выведите его первую цифру после десятичной точки.
#
# Формат входных данных
# На вход программе подаётся положительное действительное число.
#
# Формат выходных данных
# Программа должна вывести цифру в соответствии с условием задачи.
#
# Sample Input 1:
#
# 3384390.4339
# Sample Output 1:
#
# 4
# Sample Input 2:
#
# 1.5
# Sample Output 2:
#
# 5
# Sample Input 3:
#
# 459933200.23
# Sample Output 3:
#
# 2

number = input()

decimal_index = number.find('.')

if decimal_index != -1 and decimal_index + 1 < len(number):
    print(number[decimal_index + 1])
else:
    print("Нет цифр после десятичной точки.")





