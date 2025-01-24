number = input("Введите число: ")

if number.startswith('-'):
    number = number[1:]

digit_count = len(number)

print("Количество цифр в числе:", digit_count)
