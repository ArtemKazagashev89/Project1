import os
from src.generators import filter_by_currency
from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.utils import get_transactions_info_json
from src.data_reader import read_transactions_from_csv, read_transactions_from_excel
from src.transaction_processor import search_transactions, count_transaction_types

PATH_TO_FILE_JSON = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")
PATH_TO_FILE_CSV = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions.csv")
PATH_TO_FILE_EXCEL = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions_excel.xlsx")


def main():
    """Основная функция проекта"""
    while True:
        print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
        print("Выберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")

        menu_item = input()

        if menu_item == "1":
            print("Для обработки выбран JSON-файл.")
            transactions = get_transactions_info_json(PATH_TO_FILE_JSON)
            break
        elif menu_item == "2":
            print("Для обработки выбран CSV-файл.")
            transactions = read_transactions_from_csv(PATH_TO_FILE_CSV)
            break
        elif menu_item == "3":
            print("Для обработки выбран XLSX-файл.")
            transactions = read_transactions_from_excel(PATH_TO_FILE_EXCEL)
            break
        else:
            print("Такого пункта в меню нет, попробуйте еще раз.")

    state_list = ["EXECUTED", "CANCELED", "PENDING"]

    while True:
        state = input(
            """Введите статус, по которому необходимо выполнить фильтрацию. 
            Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING. """
        ).upper()

        if state not in state_list:
            print(f'Статус операции "{state}" недоступен.')
        else:
            break

    filtered_transactions = filter_by_state(transactions, state)

    date_sort = input("Отсортировать операции по дате? Да/Нет. ").lower()
    if date_sort == "да":
        if input("Отсортировать по возрастанию или по убыванию? ").lower() == "по возрастанию":
            date_flag = False
        else:
            date_flag = True
        filtered_transactions = sort_by_date(filtered_transactions, date_flag)

    filter_by_rub = input("Выводить только рублевые транзакции? Да/Нет ").lower()
    if filter_by_rub == "да":
        rub_transactions = filter_by_currency(filtered_transactions, "RUB")
        filtered_transactions = list(rub_transactions)[:-1]

    filter_by_word = input(
        "Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет "
    ).lower()
    if filter_by_word == "да":
        search_string = input("Введите слово: ")
        filtered_transactions = search_transactions(filtered_transactions, search_string)

    print("Распечатываю итоговый список транзакций...")
    if len(filtered_transactions) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
        for tr in filtered_transactions:
            tr_date = get_mask_account(tr["date"])
            currency = tr["operationAmount"]["currency"]["name"]
            if tr["description"] == "Открытие вклада":
                from_to = get_mask_card_number(tr["to"])
            else:
                from_to = get_mask_card_number(tr["from"]) + " -> " + get_mask_card_number(tr["to"])
            amount = tr["operationAmount"]["amount"]
            print(f"{tr_date} {tr['description']} {from_to} Сумма: {round(float(amount))} {currency}")


if __name__ == "__main__":
    main()
