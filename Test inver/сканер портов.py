# import subprocess
import socket
import os

# global result_open
# global result_close
# from typing import List, Any

ports = [20, 21, 22, 23, 25, 42, 43, 53, 67, 69, 80, 110, 115, 123, 137, 138, 139, 143, 161, 179, 443, 445, 514, 515,
         993, 995, 1080, 1194, 1433, 1702, 1723, 3128, 3268, 3306, 3389, 5432, 5060, 5900, 5938, 8080, 10000, 20000]
host = input('Введи имя сайта без http/https или IP-адрес: ')
# otvet = input('Ты удалил папку Результат сканирования')
# if otvet == ('Yes') or ('YES') or ('Y'):
#     cont
# else:
#     System.out.print("program terminated......");
#     System.exit(0)

print("Жди!")

# создали папку для txt
# try:
try:
    os.mkdir('Результат сканирования')
except IndentationError:
    pass
    # print("Сначала удали папку: Результат сканирования код: IndentationError")
    # os.rmdir('Результат сканирования', ignore_errors=True)
    # os.mkdir('Результат сканирования', ignore_errors=True)
except FileExistsError:
    pass
    # print("Сначала удали папку: Результат сканирования код: FileExistsError")
    # break
    # os.rmdir('Результат сканирования', ignore_errors=True)
    # os.mkdir('Результат сканирования', ignore_errors=True)
# except FileExistsError:
#     print("Удали папку: Результат сканирования")
# ('C:\\Users\\vsinenko\\PycharmProjects\\stepik\\Test inver\\отстрел2')
# C:\\Users\\%USERNAME%\\PycharmProjects\\stepik\\Test inver\\отстрел\\ второй путь
# В цикле перебираем порты из списка

for port in ports:
    # Создаем сокет
    scaner_variable = socket.socket()
    # Ставим тайм-аут
    scaner_variable.settimeout(0.0001)
    # Конструкция под ошибки
    try:
        # Пробуем соединиться, хост и порт
        scaner_variable.connect((host, port))
    except socket.error:
        # score_close = []
        # result_close: list[list[Any]] = [score_close]
        # Поймали ошибку
        print(f"{host}: {port} порт закрыт")
        port_close = open('Результат сканирования\\порты_закрыты.txt', 'a+', encoding='UTF-8')
        # C:\\Users\\vsinenko\\PycharmProjects\\stepik\\Test inver\\отстрел\\
        # ('\\Сканер портов Результат\\порты_закрыты.txt')
        port_close.write(f"{host},{port} порт закрыт \n")
        # result_close += 1
    # И пропустили её
    # pass
    else:
        print(f"{host}: {port} порт активен")
        port_open = open('Результат сканирования\\порты_открыты.txt', 'a+', encoding='UTF-8')
        # C:\\Users\\vsinenko\\PycharmProjects\\stepik\\Test inver\\отстрел\\
        # ('\\Сканер портов Результат\\порты_открыты.txt')
        port_open.write(f"{host},{port} порт активен \n")
        # result_open += 1
        scaner_variable.close
    # завершили цикл
try:
    file_open_open = open('Результат сканирования\\порты_открыты.txt', 'r', encoding='UTF-8')
    file_count_open = file_open_open.read()
    file_score_open = file_count_open.count('активен')
    print()
    print(f"Портов открыто: ", file_score_open)
    print(file_count_open)
except FileNotFoundError:
    print("Все порты закрыты")
try:
    file_open_close = open('Результат сканирования\\порты_закрыты.txt', 'r', encoding='UTF-8')
    file_count_close = file_open_close.read()
    file_score_close = file_count_close.count('закрыт')
    print()
    print(f"Портов закрыто: ", file_score_close)
except FileNotFoundError:
    print("Все порты открыты")
# print(file_count_close)

print("Сканирование завершено!")

# win_key = subprocess.check_output('ping google.com').decode().split('\n')[1].strip()

# by Verzof
