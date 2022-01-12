file_open = open('Результат сканирования\\порты_открыты.txt', 'r', encoding='UTF-8')
file_count = file_open.read()
file_score = file_count.count('активен')
print(file_score)