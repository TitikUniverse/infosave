import sys
import itertools
from string import digits, punctuation, ascii_letters, ascii_lowercase 


# 1 - Проверка пароля на соответствие заданным критериям по словарям
# 2 - Генерация пароля по заданным критериям
# 3 - Пакетная обработка файла с паролями
# 4 - Вывод отчёта о количестве проверок с делением на соответствующие и несоответствующие


def check_password(password, kol_vo_symbol, is_res, is_spec, is_number):
    lenght, up_resistor, use_punctuation, use_number = 0, False, False, False
    # slovar.txt - файл с критериями
    with open('slovar.txt', 'r') as file:
        for line in file:
            if "{" not in line and "}" not in line:
                q = line.replace(' ', '')
                q = q.split("\n")
                for i in q:
                    i = i.replace(" ", "")
                    if i:
                        if "lenght" in i.lower():
                            lenght = i.split(":")[1].split(";")[0]
                        if "up_resistor" in i.lower():
                            up_resistor = i.split(":")[1].split(";")[0]
                        if "use_punctuation" in i.lower():
                            use_punctuation = i.split(":")[1].split(";")[0]
                        if "use_number" in i.lower():
                            use_number = i.split(":")[1].split(";")[0]
        if lenght == kol_vo_symbol:
            if up_resistor == is_res:
                if use_punctuation == is_spec:
                    if use_number == is_number:
                        return 'Ваш пароль полностью совпадает с критериями :)'
                    return 'Инфо о номерах не совпадает :('
                return 'Инфо о спецсимволах не совпадает :('
            return 'Резистры не совпадают :('
        return 'Длина пароля не совпадает :('


def main():
    action = int(input('Введите номер действия: '))
    password = input('Введите пароль: ')
    kol_vo_symbol = int(input('Кол-во символов: '))

    print('Во всех остальных вопросах ответ да в любом регистре означает согласие, другие ответы - отказ')

    is_res = True if input('Использовать верхний резистер: ').lower() == "да" else False
    is_spec = True if input('Использовать спецсимволы: ').lower() == "да" else False
    is_number = True if input('Использовать числа: ').lower() == "да" else False

    possible_symbol = ""

    if is_number:
        if is_spec:
            if is_res:
                possible_symbol = digits + punctuation + ascii_letters
            else:
                possible_symbol = digits + punctuation + ascii_lowercase
        else:
            if is_res:
                possible_symbol = digits + ascii_letters
            else:
                possible_symbol = digits + ascii_lowercase
    else:
        if is_spec:
            if is_res:
                possible_symbol = punctuation + ascii_letters
            else:
                possible_symbol = punctuation + ascii_lowercase
        else:
            if is_res:
                possible_symbol = ascii_letters
            else:
                possible_symbol = ascii_lowercase

    print()

    work(action, password, kol_vo_symbol, possible_symbol, is_res, is_spec, is_number)


def work(action, password, kol_vo_symbol, possible_symbol, is_res, is_spec, is_number):
    if action == 1:
        print(check_password(password, kol_vo_symbol, is_res, is_spec, is_number))

    elif action == 2:
        with open("test.txt", "w") as file:
            for password in itertools.product(possible_symbol, repeat=kol_vo_symbol):
                password = "".join(password)
                file.write(password + '\n')

    elif action == 3:
        # slovar1.txt - словарь всех паролей
        with open('slovar1.txt', "r") as file:
            for line in file:
                line = line.replace(' ', '')
                line = line.split()[0]
                print('Пароль: ' + line + ', вердикт: ' + str(check_password(line, kol_vo_symbol, is_res, is_spec, is_number)))
    
    elif action == 4:
        itog = {
            "relevant": 0,
            "not_relevant": 0
        }
        # slovar1.txt - словарь всех паролей
        with open('slovar1.txt', "r") as file:
            for line in file:
                line = line.replace(' ', '')
                line = line.split()[0]
                if str(check_password(line, kol_vo_symbol, is_res, is_spec, is_number)) == 'Ваш пароль полностью совпадает с критериями :)':
                    w = itog['relevant'] + 1
                    itog['relevant'] = w
                else:
                    w = itog['not_relevant'] + 1
                    itog['not_relevant'] = w
        print('Кол-во соответствующих паролей: ' + str(itog['relevant']))
        print('Кол-во несоответствующих паролей: ' + str(itog['not_relevant']))

    else:
        print('Такого действия не существует, наверное вы что-то перепутали!')
        print('Попробуйте снова!')


if __name__ == "__main__":
    main()