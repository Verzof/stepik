s = 'Это обычная строка, а в ней адрес почты vasya@xakep.ru'
words = s.split()
for w in words:
    n = w.find('@xakep.ru')
    if n != -1:
        print('Найден e-mail: ' + str(w) + ' в позиции ' + str(n))