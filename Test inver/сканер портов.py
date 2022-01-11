import socket
import os

# global result_open
# global result_close
from typing import List, Any

ports = [20, 21, 22, 23, 25, 42, 43, 53, 67, 69, 80, 110, 115, 123, 137, 138, 139, 143, 161, 179, 443, 445, 514, 515,
         993, 995, 1080, 1194, 1433, 1702, 1723, 3128, 3268, 3306, 3389, 5432, 5060, 5900, 5938, 8080, 10000, 20000]
host = input('Введи имя сайта без http/https или IP-адрес: ')
print("Жди!")
# создали папку для txt
# try:
os.mkdir('Результат сканирования')
# except FileExistsError:
#     print("Удали папку: Результат сканирования")
# ('C:\\Users\\vsinenko\\PycharmProjects\\stepik\\Test inver\\отстрел2')
# C:\\Users\\%USERNAME%\\PycharmProjects\\stepik\\Test inver\\отстрел\\ второй путь
# В цикле перебираем порты из списка

for port in ports:
    # Создаем сокет
    s = socket.socket()
    # Ставим тайм-аут
    s.settimeout(0.5)
    # Конструкция под ошибки
    try:
        # Пробуем соединиться, хост и порт передаем как список
        s.connect((host, port))
    except socket.error:
        # score_close = []
        # result_close: list[list[Any]] = [score_close]
        # Поймали ошибку
        print(f"{host}: {port} порт закрыт")
        port_close = open('Результат сканирования\\порты_закрыты.txt', 'a+', encoding='UTF-8')
        # C:\\Users\\vsinenko\\PycharmProjects\\stepik\\Test inver\\отстрел\\
        # ('\\Сканер портов Результат\\порты_закрыты.txt')
        port_close.write(f"{host},{port} порт закрыт \n")
        result_close += 1
    # И пропустили её
    # pass
    else:
        print(f"{host}: {port} порт активен")
        port_open = open('Результат сканирования\\порты_открыты.txt', 'a+', encoding='UTF-8')
        # C:\\Users\\vsinenko\\PycharmProjects\\stepik\\Test inver\\отстрел\\
        # ('\\Сканер портов Результат\\порты_открыты.txt')
        port_open.write(f"{host},{port} порт активен \n")
        # result_open += 1
        s.close
    # завершили цикл
# print(result_open, result_close)
print("Сканирование завершено! by Verzof")
print(result_close)
