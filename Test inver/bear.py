# num = 1000
# # for i in range(999):
#     num = num - 1
#     print('Я ' + str(num) + ' кружка пива')


# a = 0
# while a < 100:
#     a = a + 1
#     if (a % 2) == 0:
#       print(a)

# import os
# while True:
#     a=os.fork()

# Подключим модуль для работы с буфером обмена
import pyperclip
# Подключим модуль для работы с системным временем
import time
# Задаем переменную old и присваиваем ей пустую строку
old = ''
# Начнем бесконечный цикл слежения за буфером обмена
while True:
    # Кладем в переменную s содержимое буфера обмена
    s = pyperclip.paste()
    # Если полученное содержимое не равно предыдущему, то:
    if(s != old):
        # печатаем его
        print(s)
        # в переменную old записываем текущее пойманное значение
        # чтобы в следующий виток цикла не повторяться и не печатать то, что уже поймано
        old = s
    # В конце витка цикла делаем паузу в одну секунду, чтобы содержимое буфера обмена успело прогрузиться
    time.sleep(1)