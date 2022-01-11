s1 = 'Раз, два, три, четыре, пять\n'
s2 = 'Я иду сервак ломать...\n'
f = open('poems.txt', 'w', encoding='UTF-8')
f.write(s1)
f.write(s2)
f.close()