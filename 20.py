# num = int(input())
# digit3 = num % 10
# digit2 = (num // 10) % 10
# digit1 = num // 100
# s1 = (digit1 + digit2 + digit3)
# s2 = (digit1 * digit2 * digit3)
#
# print("Сумма цифр =", s1)
# print("Произведение цифр =", s2)


a = input()
print('Сумма цифр =', int(a[0]) + int(a[1]) + int(a[2]))
print('Произведение цифр =', int(a[0]) * int(a[1]) * int(a[2]))

# a = int(input())
# n1 = a % 10            # Третья цифра
# n2 = (a % 100) // 10   # Вторая цифра
# n3 = a // 100          # Первая цифра
# print('Сумма цифр =', n1 + n2 + n3)
# print('Произведение цифр =', n1 * n2 * n3)
