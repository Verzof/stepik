# if __name__ == "__main__":
#     print(f"Я работаю как независимая программа с именем {__name__}")
# else:
#     print(f"Я работаю как импортированный модуль с именем {__name__}")
#
#
#
def say_hello(name=''):
    print(f"Hello: {name}")


def print_age(age=20):
    print(f"Age: {age}")


def main():
    name = input("Enter your name:")
    age = input("How old are you:")
    say_hello(name=name)
    print_age(age=age)
    print(f"Я работаю как независимая программа с именем {__name__}")


if __name__ == "__main__":
    main()
else:
    print(f"Я работаю как импортированный модуль с именем {__name__}")
