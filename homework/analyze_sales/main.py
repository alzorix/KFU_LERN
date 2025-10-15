'''Задание: "Система анализа продаж"
Цель: Разработать программу для анализа ежедневных продаж в магазине,
 где каждая функция должна иметь строго определённую алгоритмическую сложность.
'''


# sales будет списком кортежей: (день, сумма_продаж_в_этом_дне)
sales = []

'''add_sale(sales, amount)
Что делает: Добавляет сумму новой продажи в систему.
Требуемая сложность: O(1)
Подсказка: Используй структуру данных, позволяющую добавлять элементы в конец за постоянное время.
'''

def add_sale(sales: list, amount: float):
    day = len(sales) + 1
    sales.append((day, amount))
    return sales

'''get_total_sales(sales)
Что делает: Возвращает общую сумму всех продаж за день.
Требуемая сложность: O(n)
Подсказка: Тебе придется просуммировать все элементы. Линейная сложность здесь неизбежна и является хорошим примером.
'''
def get_total_sales(sales: list):

    target_day = sales[-1][0]
    total = sum(amount for d, amount in sales if d == target_day)
    return total

'''find_best_sales_day(sales, days)
Что делает: Находит день с максимальной общей суммой продаж. sales - это массив, где каждый элемент это массив продаж за один день.
Требуемая сложность: O(n²) в худшем случае.
Подсказка: Используй вложенные циклы. Сначала цикл по дням (n), а внутри цикл по продажам за этот день (m). В сумме O(n * m), что является частным случаем O(n²).
'''
def find_best_sales_day(sales: list, days: int):
    max_total = float("-inf")
    best_day = None
    for day_id in range(1, days + 1):
        day_total = 0
        for d, amount in sales:
            if d == day_id:
                day_total += amount
        if day_total > max_total:
            max_total = day_total
            best_day = day_id
    return best_day

'''get_unique_sale_amounts(sales)
Что делает: Возвращает список уникальных сумм продаж, которые встречались за день.
Требуемая сложность: O(n)
Подсказка: Используй множество для проверки уникальности за постоянное время.
'''
def get_unique_sale_amounts(sales: list):
    day = sales[-1][0]
    return set(amount for d, amount in sales if d == day)
