# Напишите программу, которая считывает одну строку текста и выводит
# 10
# 10 строк, пронумерованных от 0 до 9 каждая, с указанной строкой текста.
#
# На вход программе подаётся одна строка текста.
#
# Программа должна вывести 10 строк в соответствии с условием задачи.
#
# Sample Input 1:
#
# LeBron
#
# Sample Output 1:
#
# 0 LeBron
# 1 LeBron
# 2 LeBron
# 3 LeBron
# 4 LeBron
# 5 LeBron
# 6 LeBron
# 7 LeBron
# 8 LeBron
# 9 LeBron

text = input()

for i in range(10):
    print(f"{i} {text}")




