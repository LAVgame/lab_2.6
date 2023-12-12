#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    records = []

    while True:
        command = input("Введите команду (add, display, select, exit): ").lower()

        if command == 'exit':
            break
        elif command == 'add':
            record = {}
            record['расчетный счет плательщика'] = input('Введите расчетный счет плательщика: ')
            record['расчетный счет получателя'] = input('Введите расчетный счет получателя: ')
            record['перечисляемая сумма в руб.'] = float(input('Введите перечисляемую сумму в рублях: '))
            records.append(record)
            records.sort(key=lambda x: x['расчетный счет плательщика'])
            print('Запись добавлена и отсортирована.')
        elif command == 'display':
            # Вывод таблицы с данными
            line = '+-{}-+-{}-+-{}-+'.format('-'*20, '-'*20, '-'*25)
            print(line)
            print('| {:^20} | {:^20} | {:^25} |'.format("Р. счет плательщика", "Р. счет получателя", "Перечисляемая сумма"))
            print(line)
            
            for record in records:
                print('| {:<20} | {:<20} | {:>25} |'.format(record['расчетный счет плательщика'],
                                                              record['расчетный счет получателя'],
                                                              record['перечисляемая сумма в руб.']))
            print(line)
        elif command.startswith('select'):
            rc = input('Введите расчетный счет плательщика для поиска суммы: ')
            n = False

            for rec in records:
                if rec['расчетный счет плательщика'] == rc:
                    print(f"Сумма, снятая с расчетного счета плательщика {rc}: {rec['перечисляемая сумма в руб.']} руб.")
                    n= True
                    break

            if not n:
                print(f"Расчетный счет плательщика {rc} не найден.")
        else:
            print("Неверная команда. Попробуйте снова.")
