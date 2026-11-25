# Программа «Учёт книг» — версия 2
# версия содержит две намеренные ошибки 

vyidano = 0  # количество выданных книг

while True:
    print()
    print("=== Учёт книг ===")
    print("1 - Выдать книгу")
    print("2 - Показать, сколько книг выдано")
    print("3 - Сбросить счётчик")
    print("4 - Вернуть книгу")
    print("0 - Выход")
    komanda = input("Введите команду: ")

    if komanda == "1":
        vyidano = vyidano + 1
        print("Книга выдана.")
    elif komanda == "2":
        print("Сейчас выдано книг:", vyidano)
    elif komanda == "3":
        vyidano = 0
        print("Счётчик сброшен.")
    elif komanda == "4":
        # D1: нет проверки на 0 — счётчик уходит в минус
        vyidano = vyidano - 1
        print("Книга возвращена.")
    elif komanda == "0":
        print("До свидания!")
        break
    else:
        # D2: при неизвестной команде счётчик обнуляется (регрессия)
        vyidano = 0
        print("Неизвестная команда")