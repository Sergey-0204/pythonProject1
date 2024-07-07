def get_multiplied_digits(number):  #Напишите функцию get_multiplied_digits и параметр number в ней.
    str_number = str(number)  #Создайте переменную str_number и запишите строковое представление(str) числа number в неё.
    first = int(str_number[0])  # создайте переменную first и запишите в неё первый символ из str_number в числовом представлении(int).
    if len(str_number) > 1:  # функция берет первую цифру числа, преобразует ее в целое число и умножает на результат вызова той же функции для оставшихся цифр числа (вызов рекурсии).
        # Это позволяет умножать все цифры числа между собой.
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return int(str_number)  #Если же длина str_number не больше 1, тогда вернуть оставшуюся цифру first.


result = get_multiplied_digits(40203)
print(result)  # Вывод: 24
