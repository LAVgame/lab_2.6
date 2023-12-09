#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Задача 2: Использовать словарь для учета данных о переводах между счетами.

# Ввод данных с клавиатуры в список словарей
if __name__ == "__main__":
    transactions_list = []
    while True:
        payer_account = input("Введите расчетный счет плательщика (или 'конец' для завершения): ")
    
        if payer_account.lower() == 'конец':
            break
    
        recipient_account = input("Введите расчетный счет получателя: ")
        transfer_amount = float(input("Введите перечисляемую сумму в рублях: "))
    
        transaction_data = {
         'payer_account': payer_account,
            'recipient_account': recipient_account,
           'transfer_amount': transfer_amount
        }
    
        transactions_list.append(transaction_data)

    # Сортировка списка по расчетным счетам плательщиков
    transactions_list.sort(key=lambda x: x['payer_account'])

    # Вывод на экран информации о сумме, снятой с расчетного счета плательщика
    search_account = input("Введите расчетный счет плательщика для поиска суммы: ")
    found = False

    for transaction in transactions_list:
     if transaction['payer_account'] == search_account:
        print(f"Сумма, снятая с расчетного счета {search_account}: {transaction['transfer_amount']} руб.")
        found = True
        break

    if not found:
        print(f"Расчетный счет {search_account} не найден в данных.")
