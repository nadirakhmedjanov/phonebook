import os

def check_and_create_file():
    """Проверяет наличие файла и создает его с заголовками, если он не существует."""
    if not os.path.isfile('file.txt'):
        with open('file.txt', 'w', encoding='utf-8') as data:
            data.write('Фамилия Имя Номер_телефона\n')

def input_data():
    """Ввод данных для справочника и запись их в файл."""
    data_1 = input('\nВведите данные для справочника: Фамилия Имя Номер телефона (через пробел):\n')
    if len(data_1.split()) != 3:
        print("Ошибка: необходимо ввести Фамилию, Имя и Номер телефона.")
        return
    with open('file.txt', 'a', encoding='utf-8') as data:
        data.write(data_1 + '\n')

def print_data():
    """Вывод всех данных из справочника."""
    try:
        with open('file.txt', 'r', encoding='utf-8') as data:
            print('\nСодержимое справочника:')
            for line in data:
                print(line.strip())  # Убираем лишние переводы строк
    except UnicodeDecodeError:
        print("Ошибка декодирования. Проверьте кодировку файла.")

def search_data():
    """Поиск данных в справочнике."""
    try:
        with open('file.txt', 'r', encoding='utf-8') as data:
            search = input('\nВведите слово для поиска: ')
            print('\nРезультаты поиска:')
            for line in data:
                if search in line:
                    print(line.strip())  # Убираем лишние переводы строк
    except UnicodeDecodeError:
        print("Ошибка декодирования. Проверьте кодировку файла.")

def copy_data():
    """Копирование данных из file.txt в file_copy.txt."""
    if not os.path.isfile('file.txt'):
        print("Исходный файл не существует.")
        return

    with open('file.txt', 'r', encoding='utf-8') as source:
        lines = source.readlines()

    with open('file_copy.txt', 'w', encoding='utf-8') as destination:
        for line in lines:
            destination.write(line)

    print("Данные успешно скопированы в file_copy.txt.")

def main_menu():
    """Главное меню программы."""
    check_and_create_file()  # Убедимся, что файл существует при запуске программы
    print('Добро пожаловать в телефонный справочник!')
    while True:
        answer = input('1) Сделать запись\n2) Найти\n3) Вывести всё\n4) Скопировать данные\n5) Выйти\nВведите вариант: ')
        if answer == '1':
            input_data()
        elif answer == '2':
            search_data()
        elif answer == '3':
            print_data()
        elif answer == '4':
            copy_data()
        elif answer == '5':
            print('\nВсего доброго!')
            break
        else:
            print('\nТакого варианта нет.\n')

# Чистим экран перед запуском главного меню (опционально)
os.system('cls||clear')
main_menu()
