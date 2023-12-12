#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Использовать словарь, содержащий следующие ключи: расчетный счет
#плательщика; расчетный счет получателя; перечисляемая сумма в руб.
#Написать программу, выполняющую следующие действия: ввод с клавиатуры
#данных в список, состоящий из словарей заданной структуры; записи должны
#быть размещены в алфавитном порядке по расчетным счетам плательщиков;
#вывод на экран информации о сумме, снятой с расчетного счета плательщика,
#введенного с клавиатуры; если такого расчетного счета нет, выдать на дисплей
#соответствующее сообщение.


# Список для хранения данных
if __name__ == "__main__":
    records = []
    while True:
        command = input("Введите команду (add, display, exit): ").lower()

        if command == 'exit':
            break
        elif command == 'add':
         record = {}
         record['расчетный счет плательщика'] = input('Введите расчетный счет плательщика: ')
         record['расчетный счет получателя'] = input('Введите расчетный счет получателя: ')
         record['перечисляемая сумма в руб.'] = float(input('Введите перечисляемую сумму в рублях: '))
         records.append(record)
         print('Запись добавлена.')
        elif command == 'display':
            nt = input('Введите расчетный счет плательщика для поиска суммы: ')
        y = False

        for record in records:
            if record['расчетный счет плательщика'] == nt:
                print(f"Сумма, снятая с расчетного счета плательщика {nt}: {record['перечисляемая сумма в руб.']} руб.")
                y = True
                break

        if not y:
            print(f"Расчетный счет плательщика {nt} не найден.")
        else:
            print("Неверная команда. Попробуйте снова.")

    # Сортировка записей по расчетным счетам плательщиков перед выходом
    records.sort(key=lambda x: x['расчетный счет плательщика'])
