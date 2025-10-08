from functools import reduce

order_dict = {}
menu = {
    "coffee": 120,
    "tea": 80,
    "sandwich": 200,
    "cake": 150,
    "juice": 100
}

# Вывод меню, отсортированного по выбору
def print_menu():
    choose_method = int(input("1) по названию блюда (алфавит)\n2) по цене (от дешёвого к дорогому)\nВыберите: "))
    if choose_method == 1:
        sorted_food = sorted(menu.items(), key=lambda x: x[0])  # по названию
    elif choose_method == 2:
        sorted_food = sorted(menu.items(), key=lambda x: x[1])  # по цене
    else:
        print("Неверный выбор!")
        return

    for food, price in sorted_food:
        print(f"{food}: {price}")

# Средняя цена
def get_sr_price():
    sr_price = sum(menu.values()) / len(menu)
    print(f"Средняя цена: {sr_price}")

# Добавление или обновление блюда
def manage_menu():
    global menu
    data = input("Введите данные в формате 'название - цена':\n")
    name, price = map(lambda x: x.strip(), data.split("-"))
    menu.update({name: int(price)})
    print(f"Блюдо '{name}' обновлено/добавлено!")

# Удаление блюда
def delete_food():
    global menu
    name = input("Введите название блюда для удаления:\n").strip()
    print(f"Удалено {menu.pop(name)}") if name in menu else print("Такого блюда нет!")

# Фильтр блюд дешевле N
def filter_food():
    N = int(input("Введите максимальную цену N: "))
    filtered = list(filter(lambda item: item[1] <= N, menu.items()))
    print("Блюда дешевле N:", filtered)

# Минимум и максимум
def min_max_food():
    min_food = min(menu.values())
    max_food = max(menu.values())

    min_foods = [name for name, price in menu.items() if price == min_food]
    max_foods = [name for name, price in menu.items() if price == max_food]

    print("Самые недорогие блюда:", *min_foods)
    print("Самые дорогие блюда:", *max_foods)

# Только напитки
def coffee_menu():
    drinks = sorted(
        filter(lambda item: item[0] in ("coffee", "tea", "juice"), menu.items()),
        key=lambda x: x[1]
    )
    print("Напитки:", drinks)

# Создание заказа
def create_order():
    global menu
    order = list(map(lambda x: x.strip().lower(), input("Введите продукты через запятую:\n").split(",")))
    checked = list(filter(lambda food: food in menu, order))
    order_dict = {food: menu[food] for food in checked}
    print("Ваш заказ:", order_dict)
    return order_dict

# Общая стоимость
def reduce_food(order_dict):
    if not order_dict:
        print("Заказ пустой!")
        return
    price = reduce(lambda x, y: x + y, order_dict.values())
    print(f"Общая сумма заказа: {price}")

# Вывод заказа
def print_order():
    for food, price in order_dict.items():
        print(f"{food}: {price}")
    reduce_food(order_dict)

# Главное меню через match
def main():
    while True:
        print("\n=== МЕНЮ КОМАНД ===")
        print("1) Показать меню")
        print("2) Средняя цена")
        print("3) Добавить/обновить блюдо")
        print("4) Удалить блюдо")
        print("5) Фильтр по цене")
        print("6) Дешёвое/дорогое блюдо")
        print("7) Только напитки")
        print("8) Сделать заказ")
        print("9) Показать заказ")
        print("0) Выход")

        choice = input("Ваш выбор: ")

        match choice:
            case "1":
                print_menu()
            case "2":
                get_sr_price()
            case "3":
                manage_menu()
            case "4":
                delete_food()
            case "5":
                filter_food()
            case "6":
                min_max_food()
            case "7":
                coffee_menu()
            case "8":
                global order_dict
                order_dict = create_order()
            case "9":
                print_order()
            case "0":
                print("Выход...")
                break
            case _:
                print("Неверный ввод!")

if __name__ == '__main__':
    main()
