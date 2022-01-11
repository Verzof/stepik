import requests
# Делаем GET-запрос
s = requests.get('http://xakep.ru')
# Печатаем код ответа сервера
print(s.status_code)
# Печатаем HTML-код
print(s.text)