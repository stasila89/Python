file_path = "file.txt"



def show_all_records():
    with (open(file_path, 'r', encoding="utf-8")) as _data:
        for line in _data:
            phonebook_data = line.replace(";", " ")
            print(phonebook_data, end="")


def search_record(searching_data):
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if searching_data.lower() in line.split(";")[0].lower():
                print(line, end="")


def add_contact(new_contact_fio, new_contact_number):
    with open("file.txt", "a", encoding="utf-8") as f:
        f.write("\n")
        f.write(new_contact_fio.replace(" ",";"))
        f.write(";")
        f.write(new_contact_number)

def edit_record(num_col, val, new_val):
    not_find = True
    tel = []
    with open(file_path, "r", encoding="utf-8") as f:
        tel = f.readlines()
        for i in range(len(tel)):
            lst = tel[i].strip().split(";")
            if lst[num_col - 1].lower() == val.lower():
                print(*lst, end=" => ")
                lst[num_col - 1] = new_val
                print(*lst)
                tel[i] = ";".join(lst) + "\n"
                not_find = False
    if not_find:
        print("Значение {val} не найдено")
        return
    answer = input('Подтверждаете изменения (Y/n): ')
    if answer == 'Y' or answer == 'y':
        with open(file_path, 'w', encoding="utf-8") as f:
            f.writelines(tel)
        print('Изменения сохранены.')
    else:
        print('Изменение данных отменено.')

def delete_record(num_col, val):
    not_find = True
    tel = []
    with open(file_path, 'r', encoding="utf-8") as f:
        tel = f.readlines()
        i = 0
        while i < len(tel):
            lst = tel[i].strip().split(';')
            if lst[num_col - 1].lower() == val.lower():
                print(*lst)
                del tel[i]
                not_find = False
            i += 1
    if not_find:
        print(f'Значение {val} не найдено')
        return
    answer = input('Подтверждаете удаление (Y/n): ')
    if answer == 'Y' or answer == 'y':
        with open(file_path, 'w', encoding="utf-8") as f:
            f.writelines(tel)
        print('Изменения сохранены.')
    else:
        print('Удаление данных отменено.')


def main():
    fields = ('Фамилию', 'Имя', 'Отчество', 'Телефон')
    print(("""\nВыберите действие: 
1 - Показать справочник
2 - Найти контакт
3 - Добавить контакт
4 - Изменить данные
5 - Удалить данные\n"""))
    select = int(input())
    if select == 1:
        show_all_records()
    elif select == 2:
        name = input("Введите фамилию: ")
        search_record(name)
    elif select == 3:
        fio = input("Введите ФИО через пробел: ")
        number = input("Введите Номер: ")
        add_contact(fio, number)
    elif select == 4:
            column = int(input("""\nЧто поменять: 
1 - Фамилию,
2 - Имя,
3 - Отчество,
4 - Телефон\n"""))
            if 1 <= column <= 4:
                value = input(
                    f"Введите {fields[column - 1]} для изменения: ")
                new_value = input(
                    f"Введите новое значение: ")
                edit_record(column, value, new_value)
            else:
                print("Invalid field number.")
    elif select == 5:
            column = int(input("""\nЧто удалять: 
1 - Фамилию,
2 - Имя,
3 - Отчество,
4 - Телефон\n"""))
            if 1 <= column <= 4:
                value = input(
                    f"Введите {fields[column - 1]} для удаления: ")
                delete_record(column, value)
            else:
                print("Invalid field number.")

main()