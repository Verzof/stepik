mas = [ 'Это просто строка', 'https://xakep.ru', 'Еще одна строка', 'https://habr.ru' ]
for x in mas:
    if x[:5] == 'https':
        print(x)