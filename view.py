def contact_to_s():
    return input("Введите инфо для поиска: ")


def choose_mode():
    return input("Выберите режим (1 - добавить, 2 - поиск, 3 - редактирование, 4 - удаление): ")


# def new_contact():
#     name = input("Введите имя: ")
#     phone_num = input("Введите номер тел: ")
#     return f'{name} || {phone_num}'


def show_found(result):
    print("Результат поиска: ")
    for i in result:
        print (i)


def new_employee():
    name = input ("Введите имя: ")
    post = input ("Введите должность: ")
    salary = input ("Введите зарплату: ")
    phone_num = input ("Введите номер телефона: ")
    return f'{name} || {post} || {salary} || {phone_num}'


def clarification():
    return input("Введите id: ")


def error():
    print("Введено некорректное значение")