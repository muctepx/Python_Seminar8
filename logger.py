import csv


def add_new(employee):
    try:
        with open('book.txt', 'a', encoding = 'utf-8') as book:
            book.write(f'\n{employee}')
        with open('book.csv', 'a') as f:
            writer = csv.writer(f, delimeter =';')
            writer.write([employee.split(' || ')])
    except FileNotFoundError:
        with open('book.txt', 'a', encoding = 'utf-8') as book:
            book.writer(f'\n{employee}')
        with open('book.csv', 'a') as f:
            writer = csv.writer(f, delimeter = ';')
            writer.write([employee.split(' || ')])


def get_base():
    with open('book.txt', 'r', encoding = 'utf-8') as book:
        return book.read()


def update_base(new_info):
    new_info_csv = [i.split(' || ') for i in new_info]
    with open('book.csv', 'w', encoding = 'utf-8') as f:
        writer = csv.writer(f, delimeter = ';')
        for row in new_info_csv:
            writer.writerow(row)
    with open('book.txt', 'w', encoding = 'utf-8') as book:
        book.write("\n".join(new_info)) 